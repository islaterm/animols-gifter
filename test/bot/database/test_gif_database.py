"""
Module containing the tests for the bot's database
"""
import json
import os
import unittest

from bot.database.gifs import GifDatabase

__author__ = "Ignacio Slater Muñoz <islaterm@gmail.com>"
__version__ = "v0.1b1"
__since__ = "v0.1b1"


class GifDatabaseTest(unittest.TestCase):
    """
    Test set for the database
    """
    _test_db_path: str
    _existing_db: GifDatabase
    _non_existent_db: GifDatabase
    _corrupted_db: GifDatabase

    def setUp(self) -> None:
        """
        Initializes the fields to be used in the tests
        """
        self._test_db_path = "TestDB.json"

    def tearDown(self) -> None:
        """
        Deletes the files created in the tests
        """
        os.remove(self._test_db_path)

    def test_db_create(self) -> None:
        """
        Checks if the database can be created correctly
        """
        test_db = GifDatabase(self._test_db_path)
        assert test_db.gif_list == []

    def test_db_load(self) -> None:
        """
        Checks if the database can be loaded correctly from a json file.
        """
        from random import random
        with open(self._test_db_path, "w+") as json_file:
            expected_list = [str(random()), str(random()), str(random()), str(random())]
            json.dump(expected_list, json_file)
        test_db = GifDatabase(self._test_db_path)
        assert test_db.gif_list == expected_list


if __name__ == '__main__':
    unittest.main()
