import asyncio
import functools
import concurrent.futures
import time


def async_to_sync(async_func):
    @functools.wraps(async_func)
    def sync_func(*args, **kwargs):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(async_func(*args, **kwargs))
        return result

    return sync_func
