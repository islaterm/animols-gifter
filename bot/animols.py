"""
Animols Gifter bot's manager
"""
from telegram.ext import Updater


class Gifter:
    """
    Base class for @animolsgifbot.
    """
    _updater: Updater

    def __init__(self, token: str):
        """
        Initializes the bot.

        :param token:
            Bot's token
        """
        self._updater = Updater(token)

    def run(self) -> None:
        """
        Runs the bot.
        """
        self._updater.start_polling()
