import unittest
import uuid

import pytest
from telethon import TelegramClient

from bot.animols import Gifter
from secret import API_HASH, API_ID, GIFTER_TEST_TOKEN

__author__ = "Ignacio Slater Muñoz <islaterm@gmail.com>"
__version__ = "v1.0-b.4"
__since__ = "v1.0"


def test_receive_message(bot: Gifter) -> None:
    """ Test that checks the correct reception of messages by the bot.  """
    pass


@pytest.fixture
def bot(bot_token: str):
    return Gifter(bot_token)


@pytest.fixture(scope="module")
def client(api_id: int, api_hash: str) -> TelegramClient:
    a_client = TelegramClient(f"session_{str(uuid.uuid4())}", api_id, api_hash)
    a_client.start()
    return a_client


@pytest.fixture(scope="module")
def api_id() -> int:
    return API_ID


@pytest.fixture(scope="module")
def api_hash() -> str:
    return API_HASH


@pytest.fixture()
def bot_token() -> str:
    return GIFTER_TEST_TOKEN


if __name__ == '__main__':
    unittest.main()
