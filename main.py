import os

import asyncpg
from sanic import Sanic
from aioredis import create_redis_pool

from dictionary.urls import dic_bp_v1

app = Sanic("YATIM")

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
os.environ.setdefault("YATIM_SETTINGS", dir_path)
app.config.from_envvar('YATIM_SETTINGS')

app.blueprint(dic_bp_v1)


@app.listener('before_server_start')
async def register_db(app, loop):
    app.pool = await asyncpg.create_pool(
        app.config.get("DB_DSN"),
        loop=loop
    )


@app.listener('before_server_start')
async def register_cache(app, loop):
    app.cache = await create_redis_pool(
        app.config.get("CACHE_DSN"),
        loop=loop
    )


@app.listener('after_server_stop')
async def close_cache(app, loop):
    await app.cache.wait_closed()


@app.listener('after_server_stop')
async def close_connection(app, loop):
    async with app.pool as conn:
        await conn.close()


if __name__ == "__main__":
    app.run(
        host=app.config.get("HOST"),
        port=app.config.get("PORT"),
        access_log=app.config.get("ACCESS_LOG"),
        debug=app.config.get("DEBUG"),
    )
