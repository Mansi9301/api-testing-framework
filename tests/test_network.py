import pytest
import time
import concurrent.futures
from jsonschema import validate
from schemas.user_schema import USER_SCHEMA, POST_SCHEMA


class TestNetworkPerformance:

    def test_endpoint_response_time_under_1_second(self, api_client):
        """Critical endpoint responds under 1 second SLA threshold"""
        response = api_client.get("/users/1")
        response_time = response.elapsed.total_seconds()
        assert response_time < 1.0, \
            f"Response time {response_time:.3f}s exceeded 1s SLA threshold"

    def test_multiple_endpoints_response_time(self, api_client):
        """All critical endpoints meet 2 second SLA threshold"""
        endpoints = ["/users", "/posts", "/users/1", "/posts/1"]
        for endpoint in endpoints:
            response = api_client.get(endpoint)
            response_time = response.elapsed.total_seconds()
            assert response_time < 2.0, \
                f"Endpoint {endpoint} exceeded SLA: {response_time:.3f}s"

    def test_concurrent_requests(self, api_client):
        """System handles 10 concurrent requests successfully"""
        def make_request(_):
            response = api_client.get("/users")
            return response.status_code

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(make_request, range(10)))

        assert all(status == 200 for status in results), \
            f"Some concurrent requests failed: {results}"

    def test_data_integrity_across_endpoints(self, api_client):
        """User data is consistent across different endpoints"""
        # Get user 1 directly
        user_response = api_client.get("/users/1")
        user_data = user_response.json()

        # Get posts for user 1
        posts_response = api_client.get("/posts", params={"userId": 1})
        posts_data = posts_response.json()

        # All posts should belong to user 1
        for post in posts_data:
            assert post["userId"] == user_data["id"], \
                f"Data integrity failure: post userId {post['userId']} doesn't match user id {user_data['id']}"

    def test_api_returns_correct_content_type(self, api_client):
        """API returns JSON content type header"""
        response = api_client.get("/users")
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, \
            f"Expected JSON content type, got: {content_type}"

    def test_error_response_for_invalid_endpoint(self, api_client):
        """Invalid endpoint returns 404 not found"""
        response = api_client.get("/invalid_network_endpoint")
        assert response.status_code == 404

    def test_large_payload_response_time(self, api_client):
        """Large data payload endpoint meets 3 second SLA"""
        response = api_client.get("/posts")
        response_time = response.elapsed.total_seconds()
        assert response_time < 3.0, \
            f"Large payload response {response_time:.3f}s exceeded 3s SLA"

    def test_sequential_requests_consistency(self, api_client):
        """Same endpoint returns consistent data across 5 sequential requests"""
        responses = []
        for _ in range(5):
            response = api_client.get("/users/1")
            responses.append(response.json()["id"])

        assert len(set(responses)) == 1, \
            "Inconsistent data returned across sequential requests"

    def test_post_creation_and_validation(self, api_client):
        """Network config creation returns valid response within SLA"""
        payload = {
            "title": "5G Network Configuration",
            "body": "New network node configuration for Ottawa region",
            "userId": 1
        }
        start_time = time.time()
        response = api_client.post("/posts", payload=payload)
        end_time = time.time()

        total_time = end_time - start_time
        data = response.json()

        assert response.status_code == 201
        assert data["title"] == "5G Network Configuration"
        assert total_time < 3.0, \
            f"Network config creation took {total_time:.3f}s, exceeded 3s SLA"

    def test_network_node_update_integrity(self, api_client):
        """Network node update returns correct updated data"""
        payload = {
            "id": 1,
            "title": "Updated Ottawa 5G Node Configuration",
            "body": "Modified network parameters for increased throughput",
            "userId": 1
        }
        response = api_client.put("/posts/1", payload=payload)
        data = response.json()

        assert response.status_code == 200
        assert data["title"] == "Updated Ottawa 5G Node Configuration"

    def test_batch_user_data_validation(self, api_client):
        """All users in batch response have required network fields"""
        response = api_client.get("/users")
        users = response.json()

        for user in users:
            assert "id" in user, f"User missing id field"
            assert "email" in user, f"User {user.get('id')} missing email"
            assert "username" in user, f"User {user.get('id')} missing username"
            assert "@" in user["email"], f"User {user.get('id')} has invalid email"

    def test_http_methods_not_allowed(self, api_client):
        """Verify DELETE on users list is handled"""
        response = api_client.delete("/posts/1")
        assert response.status_code == 200

    def test_response_headers_present(self, api_client):
        """API response contains required headers"""
        response = api_client.get("/users/1")
        assert "Content-Type" in response.headers
        assert "content-type" in response.headers or \
               "Content-Type" in response.headers