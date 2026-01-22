import pytest

@pytest.mark.asyncio
async def test_register_login(client):
    r = await client.post("/auth/register", json={
        "email": "a@test.com",
        "password": "pass"
    })
    assert r.status_code == 200

    r = await client.post("/auth/login", data={
        "username": "a@test.com",
        "password": "pass"
    })
    assert "access_token" in r.json()
