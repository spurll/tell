#!/usr/bin/env python

# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.


from requests import post
from argparse import ArgumentParser
import re

import config


def determine_destination(destination):
    candidates = []

    pattern = re.compile(r"{}".format(destination), re.IGNORECASE)

    for i in list_users() + list_channels():
        match = re.search(pattern, i["name"])

        # Users have a "real name" in addition to their user name.
        if not match and "real" in i:
            match = re.search(pattern, i["real"])

        if match: candidates.append(i["id"])

    if len(candidates) == 1:
        return candidates[0]

    if not candidates:
        print 'Error: No users or channels named "{}".'.format(destination)
    else:
        print "Error: Unable to identify destination. Possible matches: {}"   \
              .format(", ".join(candidates))

    return None


def send_message(destination, message):
    payload = {"token": config.TOKEN,
               "channel": destination,
               "username": config.USER,
               "icon_url": config.ICON_URL,
               "text": message}
    r = post("https://slack.com/api/chat.postMessage", data=payload)

    if check_response(r):
        print "Message delivered to {}.".format(destination)


def list_users():
    users = []

    payload = {"token": config.TOKEN}
    r = post("https://slack.com/api/users.list", data=payload)

    if check_response(r):
        users = [{"slack_id": m["id"],
                  "id": "@{}".format(m["name"]),
                  "name": m["name"],
                  "real": m["real_name"]}
                 for m in r.json()["members"]]

    return users


def list_channels():
    channels = []

    payload = {"token": config.TOKEN, "exclude_archived": 1}
    r = post("https://slack.com/api/channels.list", data=payload)

    if check_response(r):
        channels = [{"slack_id": c["id"],
                     "id": "#{}".format(c["name"]),
                     "name": c["name"]}
                    for c in r.json()["channels"]]

    return channels


def check_response(r):
    # Check the HTTP response.
    if r.status_code != 200:
        print "HTTP Code {}: {}".format(r.status_code, r.text)
        return False

    # Request was successful. Now check Slack's response.
    if not r.json()["ok"]:
        print "Slack Error: {}".format(r.json()["error"])
        return False

    return True


if __name__ == "__main__":
    parser = ArgumentParser(description="Sends a message via Terminal to a "
                            "user or channel in Slack.")
    parser.add_argument("destination", help="Where to send the message. Can "
                        "be either #channel or @user (or use neither # nor @ "
                        "and we'll try to figure out what you mean).")
    parser.add_argument("message", help="The text to send.", nargs="+")
    args = parser.parse_args()

    if args.destination and args.destination[0] not in ["#", "@"]:
        args.destination = determine_destination(args.destination)

    if args.destination and args.message:
        send_message(args.destination, " ".join(args.message))
    else:
        print "Error: You must supply both a destination and a message."

