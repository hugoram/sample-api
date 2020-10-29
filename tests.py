import falcon
import pytest
from falcon import testing
from main import app


@pytest.fixture
def client():
    return testing.TestClient(app)


def test_root_path(client):
    response = client.simulate_get("/")
    assert response.status == falcon.HTTP_OK
    assert response.content.decode() == "Hello World"
