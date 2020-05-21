import asyncio
import os

import asyncpg
from sanic import Sanic

from dictionary.urls import dic_bp_v1

app = Sanic("YATIM")
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
os.environ.setdefault("YATIM_SETTINGS", dir_path)
app.config.from_envvar('YATIM_SETTINGS')
app.blueprint(dic_bp_v1)


async def init_pool():
    app.config["pool"] = await asyncpg.create_pool(app.config["DB_DSN"])

loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_pool())

if __name__ == "__main__":
    app.run()
