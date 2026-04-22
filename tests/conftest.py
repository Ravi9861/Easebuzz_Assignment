import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client():
    return requests.Session()