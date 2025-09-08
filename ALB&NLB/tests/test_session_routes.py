import pytest

from backend.main import app as flask_app


@pytest.fixture()
def client():
    flask_app.config.update({"TESTING": True, "SECRET_KEY": "test"})
    with flask_app.test_client() as client:
        yield client


def test_home_without_login(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"You are not logged in" in res.data


def test_login_and_home(client):
    res = client.post("/login", data={"username": "alice"}, follow_redirects=True)
    assert res.status_code == 200
    assert b"Logged in as alice" in res.data


def test_logout(client):
    client.post("/login", data={"username": "bob"}, follow_redirects=True)
    res = client.get("/logout", follow_redirects=True)
    assert res.status_code == 200
    assert b"You are not logged in" in res.data


