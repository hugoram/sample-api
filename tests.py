import falcon
import json
import pytest
from falcon import testing
from unittest.mock import patch

from main import app


@pytest.fixture
def client():
    return testing.TestClient(app)


def test_root_path(client):
    response = client.simulate_get("/")
    assert response.status == falcon.HTTP_OK
    assert response.content.decode() == "Hello World"


@patch("requests.get")
def test_weather_path(get_mock, client):
    get_mock.return_value.json.side_effect = [
        [{"woeid": "some_id"}],
        {
            "title": "Mexico City",
            "timezone": "America/Mexico_City",
            "consolidated_weather": [
                {
                    "min_temp": 16,
                    "max_temp": 25,
                    "the_temp": 20,
                    "applicable_date": "2020-10-29",
                }
            ],
        },
    ]

    response = client.simulate_get("/weather/mex")
    assert response.status == falcon.HTTP_OK
    assert response.content.decode() == json.dumps(
        {
            "location": "Mexico City",
            "timezone": "America/Mexico_City",
            "date": "2020-10-29",
            "min_temp": "16°C",
            "max_temp": "25°C",
            "average_temp": "20°C",
        }
    )


@patch("requests.get")
def test_weather_path_with_not_found_result(get_mock, client):
    get_mock.return_value.json.return_value = []

    response = client.simulate_get("/weather/somethingbad")
    assert response.status == falcon.HTTP_404
    assert response.content.decode() == json.dumps(
        {"message": "The location you are looking for could not be found."}
    )


@patch("requests.get")
def test_weather_path_handles_exception(get_mock, client):
    get_mock.return_value.json.return_value = Exception()

    response = client.simulate_get("/weather/somethingverybad")
    assert response.status == falcon.HTTP_500
    assert response.content.decode() == json.dumps(
        {"message": "There was a problem retrieving the weather. Try again later."}
    )
