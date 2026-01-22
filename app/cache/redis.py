# TEMPORARY IN-MEMORY CACHE (Python 3.13 compatible)

_cache = {}


async def get_cache(key: str):
    return _cache.get(key)


async def set_cache(key: str, value, ttl: int = 300):
    _cache[key] = value


async def invalidate_cache(prefix: str):
    keys = [k for k in _cache if k.startswith(prefix)]
    for k in keys:
        _cache.pop(k, None)
# alias for compatibility with existing imports
async def invalidate(prefix: str):
    await invalidate_cache(prefix)
# alias for compatibility with existing imports
async def invalidate(prefix: str):
    await invalidate_cache(prefix)
