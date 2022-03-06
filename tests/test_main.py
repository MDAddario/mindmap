import pytest

from bin import main, persistance

# Delete pre-existing data
persistance.file_db.unlink(missing_ok=True)


@pytest.fixture()
def app():

    main.app.config.update({
        "TESTING": True,
    })

    yield main.app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_post_id(client):

    response = client.post("/", json={"id": "vegetables"})
    assert response.status_code == 200

    response = client.post("/", json={"id": "vegetables"})
    assert response.status_code == 400

    response = client.post("/", json={"id": "fruits"})
    assert response.status_code == 200

    response = client.post("/", json={"id": "fruits"})
    assert response.status_code == 400


def test_post_leaf(client):

    response = client.post("/candy", json={
        "path": "i/like/candy",
        "text": "we have no candy tree"
        })
    assert response.status_code == 400

    response = client.post("/vegetables", json={
        "path": "i/like/green/peppers",
        "text": "stuff them with rice"
        })
    assert response.status_code == 200

    response = client.post("/vegetables", json={
        "path": "i/like/green/salads",
        "text": "they're healthy"
        })
    assert response.status_code == 200

    response = client.post("/vegetables", json={
        "path": "i/hate/cauliflower",
        "text": "what a strange veggie"
        })
    assert response.status_code == 200

    response = client.post("/vegetables", json={
        "path": "i/hate/brocoli",
        "text": "small trees"
        })
    assert response.status_code == 200


def test_get_leaf(client):

    response = client.get("/vegetables/i/like/green/peppers")
    assert response.json == {
        "path": "i/like/green/peppers",
        "text": "stuff them with rice"
        }

    response = client.get("/vegetables/i/hate/brocoli")
    assert response.json == {
        "path": "i/hate/brocoli",
        "text": "small trees"
        }


def test_get_tree(client):
    response = client.get("/vegetables")
    assert response.data == b"""root/
\ti/
\t\tlike/
\t\t\tgreen/
\t\t\t\tpeppers
\t\t\t\tsalads
\t\thate/
\t\t\tcauliflower
\t\t\tbrocoli
"""
