"""
This module contains the implementation of the database driver for the bot
"""
from typing import List

__author__ = "Ignacio Slater Muñoz <islaterm@gmail.com>"
__version__ = "v0.1b1"
__since__ = "v0.1b1"


class GifDatabase:
    """

    """
    _gif_list: List[str]

    def __init__(self, path: str):
        self._gif_list = []

    @property
    def gif_list(self):
        return self._gif_list

    def add_gifs(self, *gifs: str):
        pass
