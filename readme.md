tell.py
=======

Sends a message via Terminal to a user or channel in Slack.

Installation
============

Configuration
-------------

You'll need to create a file called `config.py` containing your token (obtained from http://api.slack.com), the desired user name for your bot, and the URL of the image you'd like to use for its avatar. For example:

```python
TOKEN = 'XXXX-XXXX-XXXX-XXXX-XXXX'
USER = 'BotName'
ICON_URL = 'https://secure.gravatar.com/avatar/AVATAR_URL.jpg'
```

Requirements
------------

* Slack (this one is sort of key)
* requests

Running from Spotlight
======================

`Tell.app` allows you to run tell from Spotlight on OS X. You'll need to open `Tell.scpt` and edit this line to point to the appropriate location:

```applescript
set tell_script to "~/Development/tell/tell.py"
```

Export the script as an Application and copy `Tell.app` into your Applications directory.

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

For more information about Slack, visit:
http://www.slack.com

For more information about the Slack API, visit:
http://api.slack.com

License Information
===================

Written by Gem Newman.
http://www.startleddisbelief.com

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

