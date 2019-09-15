import unittest

from bot.animols import Gifter

__author__ = "Ignacio Slater Muñoz <islaterm@gmail.com>"
__version__ = "v0.1b3"
__since__ = "v0.1b3"


class GifterTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        Initializes the fields needed for the tests
        """
        from secret import GIFTER_TEST_TOKEN
        self._bot = Gifter(GIFTER_TEST_TOKEN)

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
