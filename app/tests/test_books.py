import pytest


@pytest.mark.asyncio
async def test_books_requires_auth(client):
    r = await client.get("/books")
    assert r.status_code == 401
