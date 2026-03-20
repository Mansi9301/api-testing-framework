import pytest
from jsonschema import validate
from schemas.user_schema import USER_SCHEMA, USERS_LIST_SCHEMA


class TestUsers:

    def test_get_all_users_status_code(self, api_client):
        """GET /users returns 200 OK"""
        response = api_client.get("/users")
        assert response.status_code == 200

    def test_get_all_users_returns_list(self, api_client):
        """GET /users returns a list of users"""
        response = api_client.get("/users")
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_get_all_users_schema(self, api_client):
        """GET /users response matches expected schema"""
        response = api_client.get("/users")
        data = response.json()
        validate(instance=data, schema=USERS_LIST_SCHEMA)

    def test_get_single_user_status_code(self, api_client):
        """GET /users/1 returns 200 OK"""
        response = api_client.get("/users/1")
        assert response.status_code == 200

    def test_get_single_user_schema(self, api_client):
        """GET /users/1 response matches expected schema"""
        response = api_client.get("/users/1")
        data = response.json()
        validate(instance=data, schema=USER_SCHEMA)

    def test_get_single_user_correct_id(self, api_client):
        """GET /users/1 returns user with id 1"""
        response = api_client.get("/users/1")
        data = response.json()
        assert data["id"] == 1

    def test_get_single_user_has_email(self, api_client):
        """GET /users/1 returns user with valid email"""
        response = api_client.get("/users/1")
        data = response.json()
        assert "@" in data["email"]

    def test_get_nonexistent_user(self, api_client):
        """GET /users/999 returns 404"""
        response = api_client.get("/users/999")
        assert response.status_code == 404

    def test_get_user_response_time(self, api_client):
        """GET /users/1 responds within 2 seconds"""
        response = api_client.get("/users/1")
        assert response.elapsed.total_seconds() < 2.0

    def test_filter_users_by_username(self, api_client):
        """GET /users?username=Bret returns correct user"""
        response = api_client.get("/users", params={"username": "Bret"})
        data = response.json()
        assert len(data) == 1
        assert data[0]["username"] == "Bret"