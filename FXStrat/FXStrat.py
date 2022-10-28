import requests as req

print("requests")


from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient

import asyncio
import json

client = easy_client(
        api_key='APIKEY',
        redirect_uri='https://localhost/',
        token_path='/tmp/token.json')
stream_client = StreamClient(client, account_id=1234567890)

async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)

    def print_message(message):
      print(json.dumps(message, indent=4))

    # Always add handlers before subscribing because many streams start sending
    # data immediately after success, and messages with no handlers are dropped.
    stream_client.add_nasdaq_book_handler(print_message)
    await stream_client.nasdaq_book_subs(['GOOG'])

    while True:
        await stream_client.handle_message()

asyncio.run(read_stream())