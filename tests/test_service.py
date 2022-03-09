"""
Unit test suite for mind map web service
Tests all endpoints made available in service/main.py
"""

import pytest

from service import main, persistance

'''
Note that this code implicity tests the persistance
of the mindmap app because a session is not created
and preserved across tests
'''

# Delete pre-existing data
persistance.file_db.unlink(missing_ok=True)


# Mandatory Pytest fixture
@pytest.fixture()
def app():
    main.app.config.update({"TESTING": True})
    yield main.app


# Mandatory Pytest fixture
@pytest.fixture()
def client(app):
    return app.test_client()


def test_post_id(client):
    """
    Unit test specification 1
    """

    # Create ID
    response = client.post("/", json={"id": "vegetables"})
    assert response.status_code == 200
    assert response.data == b'Mind map creation successful.'

    # Ensure ID cannot be duplicated
    response = client.post("/", json={"id": "vegetables"})
    assert response.status_code == 400
    assert response.data == b'ID "vegetables" already has a mind map.'

    # Create another ID
    response = client.post("/", json={"id": "fruits"})
    assert response.status_code == 200
    assert response.data == b'Mind map creation successful.'

    # Ensure ID cannot be duplicated
    response = client.post("/", json={"id": "fruits"})
    assert response.status_code == 400
    assert response.data == b'ID "fruits" already has a mind map.'


def test_post_leaf(client):
    """
    Unit test specification 2
    """

    # Test missing ID
    response = client.post("/candy", json={
        "path": "i/like/candy",
        "text": "we have no candy tree"
        })
    assert response.status_code == 400
    assert response.data == b'ID "candy" does not have a mind map.'

    # Add complex leaf
    response = client.post("/vegetables", json={
        "path": "i/like/green/peppers",
        "text": "stuff them with rice"
        })
    assert response.status_code == 200
    assert response.data == b'Mind map leaf addition successful.'

    # Add complex leaf
    response = client.post("/vegetables", json={
        "path": "i/like/green/salads",
        "text": "they're healthy"
        })
    assert response.status_code == 200
    assert response.data == b'Mind map leaf addition successful.'

    # Add complex leaf
    response = client.post("/vegetables", json={
        "path": "i/hate/cauliflower",
        "text": "what a strange veggie"
        })
    assert response.status_code == 200
    assert response.data == b'Mind map leaf addition successful.'

    # Add complex leaf
    response = client.post("/vegetables", json={
        "path": "i/hate/brocoli",
        "text": "small trees"
        })
    assert response.status_code == 200
    assert response.data == b'Mind map leaf addition successful.'

    # Overwrite text of existing leaf
    response = client.post("/vegetables", json={
        "path": "i/hate/brocoli",
        "text": "we can overwrite the text"
        })
    assert response.status_code == 200
    assert response.data == b'Mind map leaf addition successful.'


def test_get_leaf(client):
    """
    Unit test specification 3
    """

    # Test missing ID
    response = client.get("/candy/i/like/candy/corn")
    assert response.status_code == 400
    assert response.data == b'ID "candy" does not have a mind map.'

    # Get text from leaf
    response = client.get("/vegetables/i/like/green/peppers")
    assert response.json == {
        "path": "i/like/green/peppers",
        "text": "stuff them with rice"
        }

    # Get overwritten text from leaf
    response = client.get("/vegetables/i/hate/brocoli")
    assert response.json == {
        "path": "i/hate/brocoli",
        "text": "we can overwrite the text"
        }

    # Try inexistent path
    response = client.get("/vegetables/i/like/orange/plums")
    assert response.status_code == 400
    assert response.data == b'Path "i/like/orange/plums" does not exist in "vegetables" mind map.'


def test_get_tree(client):
"""
    Unit test specification 4
    """

    # Test missing ID
    response = client.get("/candy")
    assert response.status_code == 400
    assert response.data == b'ID "candy" does not have a mind map.'

    # Pretty print empty ID
    response = client.get("/fruits")
    assert response.data == b'root'

    # Pretty print complex ID
    response = client.get("/vegetables")
    assert response.data == b"""root/
\ti/
\t\tlike/
\t\t\tgreen/
\t\t\t\tpeppers
\t\t\t\tsalads
\t\thate/
\t\t\tcauliflower
\t\t\tbrocoli"""
