import ujson
from sanic.response import json


def cache(method):
    async def cached(*args, **kwargs):
        key = "{0}_{1}".format(
            method.__name__,
            "_".join(
                list(
                    map(str, kwargs.values())
                )
            )
        )
        result = await args[0].app.cache.get(key)
        if not result:
            result = await method(*args, **kwargs)
            await args[0].app.cache.set(
                key,
                ujson.dumps(result),
                expire=args[0].app.config.get("CACHE_EXPIRE_TIME")
            )
            return json(result)
        return json(ujson.loads(result))
    return cached
