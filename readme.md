Tell
====

Sends a message via Terminal to a user or channel in Slack. It's basically just a really simple command-line wrapper for [SlackUtils](https://github.com/spurll/slackutils/).

Mark
====

Marks all Slack channels and private groups as read.

Installation
============

Configuration
-------------

You'll need to create a file called `config.py` containing your token (which can be obtained from the [Slack API page](http://api.slack.com)), the desired user name for your bot, and the URL of the image you'd like to use for its avatar. For example:

```python
TOKEN = 'XXXX-XXXX-XXXX-XXXX-XXXX'
USER = 'BotName'
ICON_URL = 'https://secure.gravatar.com/avatar/AVATAR_URL.jpg'
```

Requirements
------------

* [slackutils](https://github.com/spurll/slackutils/)

Running from Spotlight
----------------------

`Tell.app` allows you to run tell from Spotlight on OS X. You'll need to open `Tell.scpt` and edit this line to point to the appropriate location:

```applescript
set tell_script to "~/Development/tell/tell.py"
```

Export the script as an Application and copy `Tell.app` into your Applications directory.

(`Mark.app` works similarly.)

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

None

Slack
=====

Information about Slack is available on [their website](http://www.slack.com). Information about the Slack API is available [here](http://api.slack.com).

License Information
===================

Written by Gem Newman. [GitHub](https://github.com/spurll/) | [Blog](http://www.startleddisbelief.com) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
