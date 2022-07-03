# Fluent Python 2 ch. 21

# 783 probe domains

import asyncio

async def probe(domain):
    pass

async def main():
    pass

if __name__ == '__main__':
    asyncio.run(main())


# py docs
import asyncio

async def main():
    print("hello, please wait 2 seconds.")
    await asyncio.sleep(2)
    print("world")

asyncio.run(main())

# calling main() returns a coroutine, which is what asyncio.run() expects

await suspends the current coroutine object.
the event loop then drives other pending coroutine objects.

await works with awaitables (compare to 'for', which works with iterables)

an asyncio.Task is passed to asyncio.create_task()

the HTTPX client has asynchronous HTTP download functions


import asyncio

from httpx import AsyncClient

async def get_flag(client):
    resp = await client.get(url)
    return resp.read()


# asyncpg
async with connection.transaction():
    await connection.execute("insert into tbl (col1) values ('abc');")
