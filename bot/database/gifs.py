"""
This module contains the implementation of the database driver for the bot
"""
from json import JSONDecodeError
from typing import List

__author__ = "Ignacio Slater Muñoz <islaterm@gmail.com>"
__version__ = "v0.1b1"
__since__ = "v0.1b1"


class GifDatabase:
    """
    Database to hold the list of gifs stored by the bot
    """
    _gif_list: List[str]

    def __init__(self, path: str):
        """
        Loads a database or creates it if it doesn't exist
        :param path:
            the location of the database
        """
        try:
            import json
            with open(path, 'r') as json_file:
                self._gif_list = json.load(json_file)
        except (JSONDecodeError, FileNotFoundError):
            open(path, 'w+')
            self._gif_list = []

    @property
    def gif_list(self):
        return self._gif_list

    def add_gif(self, gif: str):
        pass
