#!/usr/bin/env python
"""
AnimolsGifter Bot's run script
"""
from bot.animols import Gifter
from secret import GIFTER_TOKEN

__author__ = "Ignacio Slater Muñoz <islaterm@gmail.com>"
__version__ = "0.1b1"

if __name__ == "__main__":
    BOT = Gifter(GIFTER_TOKEN)
    # BOT.run()
