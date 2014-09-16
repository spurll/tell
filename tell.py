#!/usr/bin/env python

# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.


from requests import post
from argparse import ArgumentParser
from slackutils import Slack
import re

import config


def main():
    parser = ArgumentParser(description="Sends a message via Terminal to a "
                            "user or channel in Slack.")
    parser.add_argument("destination", help="Where to send the message. Can "
                        "be either #channel or @user (or use neither # nor @ "
                        "and we'll try to figure out what you mean).")
    parser.add_argument("message", help="The text to send.", nargs="+")
    args = parser.parse_args()

    s = Slack(config.TOKEN, name=config.USER, icon=config.ICON_URL,
              verbose=True)
    s.send(args.destination, " ".join(args.message))


if __name__ == "__main__":
    main()

