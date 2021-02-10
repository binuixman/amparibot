#!/usr/bin/python3

from irc_class import *
import os
import random
from cheapshark_query import *

## IRC Config
server = "irc.cs.hut.fi" # Provide a valid server IP/Hostname
port = 6668
channel = "#polygame"
botnick = "amparibot"
irc = IRC()
irc.connect(server, port, channel, botnick)

freegames = get_free_games()

while True:
    text = irc.get_response()
    print(text)

    if "PRIVMSG" in text and channel in text and "ämpäri?" in text:
        header = ":Tämän päivän ämpärit: "
        irc.send(channel, header)

        for game in freegames:
            amparit = ":" + str(game[0]) + " " + str("(") + str(game[1]) + str(")")
            irc.send(channel, amparit)
