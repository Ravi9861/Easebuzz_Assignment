import requests
import json
import os

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts():
    try:
        response = requests.get(BASE_URL, timeout=5)

        # Validate status code
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        posts = response.json()

        # Validate schema keys
        required_keys = {"userId", "id", "title", "body"}

        for post in posts:
            assert required_keys.issubset(post.keys()), f"Missing keys in post: {post}"

        # Save first 5 posts
        os.makedirs("api/data", exist_ok=True)
        with open("api/data/first_5_posts.json", "w") as f:
            json.dump(posts[:5], f, indent=4)

        print("API validation successful and file saved.")

    except Exception as e:
        print(f" Error: {e}")
