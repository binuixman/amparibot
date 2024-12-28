#!/usr/bin/python3

from irc_class import *
import os
import random
import time
from cheapshark_query import *

## IRC Config
server = ""      # IRC server address goes here
port = 6667      # Server port
channel = ""     # Channel to join goes here
botnick = "amparibot"
irc = IRC()
irc.connect(server, port, channel, botnick)

freegames = get_free_games()
most_recent = time.time()
interval = 300  # Query interval in seconds

while True:
    text = irc.get_response()
    print(text)

    if "PRIVMSG" in text and channel in text and "ämpäri?" in text:
        curr = time.time()
        if curr - most_recent > interval:
            freegames = get_free_games()
            most_recent = curr
        if len(freegames) == 0:
            header = "Ämpäreitä ei löytynyt :("
            irc.send(channel, header)
            continue
        
        header = ":Tämän päivän ämpärit: "
        irc.send(channel, header)

        for game in freegames:
            amparit = ":" + str(game[0]) + " " + str("(") + str(game[1]) + str(")")
            irc.send(channel, amparit)
