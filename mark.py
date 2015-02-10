#!/usr/bin/env python

# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.


from requests import post
from argparse import ArgumentParser
from slackutils import Slack
import re

import config


def main():
    """
    Marks all of a user's slack channels as read.
    """

    s = Slack(config.TOKEN, name=config.USER, verbose=True)
    s.channels()
    s.groups()

    for c in s.channel_list:
        if c["is_member"]:
            s.mark("#" + c["name"])

    for g in s.group_list:
        s.mark(g["name"])


if __name__ == "__main__":
    main()

