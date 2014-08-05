tell.py
=======

Sends a message via Terminal to a user or channel in Slack.

Installation
============

Configuration
-------------

You'll need to create a file called `config.py` containing your token (obtained from http://api.slack.com), the desired user name for your bot, and the URL of the image you'd like to use for its avatar. For example:

```
TOKEN = 'XXXX-XXXX-XXXX-XXXX-XXXX'
USER = 'BotName'
ICON_URL = 'https://secure.gravatar.com/avatar/AVATAR_URL.jpg'
```

Requirements
------------

* Slack (this one is sort of key)
* requests
* 

Running from Spotlight
======================
To run tell from spotlight on OS X, open `AppleScript Editor` and past in the following code:
```applescript
set channel to the text returned of (display dialog "Channel" default answer "")
if channel is equal to "" then return

set message to the text returned of (display dialog "Message" default answer "")
if channel is equal to "" then return

set tell_script to "tell"
do shell script tell & " " & (quoted form of channel) & " " & (quoted form of message)
```

Save the script, choosing to save it as an Application instead of a Script. This script assumes that you have already put tell on the system path. as tell. Either `mv tell.py /usr/local/bin/tell; chmod +x /usr/local/bin/tell` or change the contents of the variable `tell_script` (remember that the path will need to be absolute).

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

