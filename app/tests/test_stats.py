import pytest
from datetime import datetime, timedelta

@pytest.mark.asyncio
async def test_stats_requires_auth(client):
    response = await client.get("/stats")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_stats_returns_valid_structure(client):
    # register user
    await client.post("/auth/register", json={
        "email": "stats@test.com",
        "password": "password"
    })

    # login
    login = await client.post("/auth/login", data={
        "username": "stats@test.com",
        "password": "password"
    })
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # call stats
    response = await client.get("/stats", headers=headers)

    assert response.status_code == 200
    data = response.json()

    # validate response shape
    assert "total_books" in data
    assert "completed" in data
    assert "streak" in data
    assert "avg_pages_per_day" in data
    assert "top_author" in data


@pytest.mark.asyncio
async def test_stats_with_books(client):
    # register user
    await client.post("/auth/register", json={
        "email": "books@test.com",
        "password": "password"
    })

    # login
    login = await client.post("/auth/login", data={
        "username": "books@test.com",
        "password": "password"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # add books
    await client.post("/books", json={
        "title": "Book One",
        "author": "Author A",
        "pages": 350
    }, headers=headers)

    await client.post("/books", json={
        "title": "Book Two",
        "author": "Author A",
        "pages": 120
    }, headers=headers)

    # get stats
    response = await client.get("/stats", headers=headers)
    data = response.json()

    assert data["total_books"] == 2
    assert data["completed"] == 1
    assert data["top_author"] == "Author A"
