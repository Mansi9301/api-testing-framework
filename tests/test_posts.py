import pytest
from jsonschema import validate
from schemas.user_schema import POST_SCHEMA, POSTS_LIST_SCHEMA


class TestPosts:

    def test_get_all_posts_status_code(self, api_client):
        """GET /posts returns 200 OK"""
        response = api_client.get("/posts")
        assert response.status_code == 200

    def test_get_all_posts_returns_100_items(self, api_client):
        """GET /posts returns exactly 100 posts"""
        response = api_client.get("/posts")
        data = response.json()
        assert len(data) == 100

    def test_get_all_posts_schema(self, api_client):
        """GET /posts response matches expected schema"""
        response = api_client.get("/posts")
        data = response.json()
        validate(instance=data, schema=POSTS_LIST_SCHEMA)

    def test_get_single_post_status_code(self, api_client):
        """GET /posts/1 returns 200 OK"""
        response = api_client.get("/posts/1")
        assert response.status_code == 200

    def test_get_single_post_schema(self, api_client):
        """GET /posts/1 matches expected schema"""
        response = api_client.get("/posts/1")
        data = response.json()
        validate(instance=data, schema=POST_SCHEMA)

    def test_get_posts_by_user(self, api_client):
        """GET /posts?userId=1 returns only posts for user 1"""
        response = api_client.get("/posts", params={"userId": 1})
        data = response.json()
        assert len(data) > 0
        for post in data:
            assert post["userId"] == 1

    def test_create_post_status_code(self, api_client):
        """POST /posts returns 201 Created"""
        payload = {
            "title": "Network Test Report",
            "body": "Automated test case for post creation",
            "userId": 1
        }
        response = api_client.post("/posts", payload=payload)
        assert response.status_code == 201

    def test_create_post_returns_correct_data(self, api_client):
        """POST /posts returns the created post with correct fields"""
        payload = {
            "title": "5G Network Validation",
            "body": "Testing network endpoint response",
            "userId": 1
        }
        response = api_client.post("/posts", payload=payload)
        data = response.json()
        assert data["title"] == "5G Network Validation"
        assert data["userId"] == 1
        assert "id" in data

    def test_update_post_status_code(self, api_client):
        """PUT /posts/1 returns 200 OK"""
        payload = {
            "id": 1,
            "title": "Updated Network Report",
            "body": "Updated test content",
            "userId": 1
        }
        response = api_client.put("/posts/1", payload=payload)
        assert response.status_code == 200

    def test_update_post_returns_updated_data(self, api_client):
        """PUT /posts/1 returns post with updated title"""
        payload = {
            "id": 1,
            "title": "Updated 5G Test Report",
            "body": "Updated content",
            "userId": 1
        }
        response = api_client.put("/posts/1", payload=payload)
        data = response.json()
        assert data["title"] == "Updated 5G Test Report"

    def test_delete_post_status_code(self, api_client):
        """DELETE /posts/1 returns 200 OK"""
        response = api_client.delete("/posts/1")
        assert response.status_code == 200

    def test_get_nonexistent_post(self, api_client):
        """GET /posts/999 returns 404"""
        response = api_client.get("/posts/999")
        assert response.status_code == 404

    def test_post_response_time(self, api_client):
        """GET /posts/1 responds within 2 seconds"""
        response = api_client.get("/posts/1")
        assert response.elapsed.total_seconds() < 2.0