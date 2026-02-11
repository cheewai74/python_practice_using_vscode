import pytest
from pip._vendor import requests


@pytest.mark.duckduckgo
@pytest.mark.rest.api
def test_duckduckgo_instant_answer_api():
    # Arrange
    url = "https://duckduckgo.com/?q=python+programming&format=json"

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']
