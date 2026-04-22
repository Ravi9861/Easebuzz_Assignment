import pytest
import time
from utils.schema import PostSchema

BASE_URL = "https://jsonplaceholder.typicode.com"

# ✅ Response Time Test
def test_response_time(api_client):
    start = time.time()
    response = api_client.get(f"{BASE_URL}/posts")
    end = time.time()

    assert response.status_code == 200
    assert (end - start) < 2, "Response time exceeded 2 seconds"


# ✅ Schema Validation
def test_schema_validation(api_client):
    response = api_client.get(f"{BASE_URL}/posts")
    posts = response.json()

    for post in posts:
        PostSchema(**post)


# ✅ Parameterized Test
@pytest.mark.parametrize("endpoint", ["posts", "comments", "users"])
def test_multiple_endpoints(api_client, endpoint):
    response = api_client.get(f"{BASE_URL}/{endpoint}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
