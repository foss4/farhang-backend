import asyncio

import asyncpg
from sanic import Sanic

from dictionary.urls import dic_bp_v1
from settings import ACCESS_LOG, DB_DSN, DEBUG, HOST, PORT

app = Sanic(__name__)
app.blueprint(dic_bp_v1)


async def init_pool():
    app.config["pool"] = await asyncpg.create_pool(DB_DSN)

loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_pool())

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG, access_log=ACCESS_LOG)
