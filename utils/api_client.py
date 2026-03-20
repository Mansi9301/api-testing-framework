import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:
    """Base API client for making HTTP requests"""

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint, params=None):
        """Makes a GET request"""
        response = self.session.get(
            f"{self.base_url}{endpoint}",
            params=params
        )
        return response

    def post(self, endpoint, payload=None):
        """Makes a POST request"""
        response = self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload
        )
        return response

    def put(self, endpoint, payload=None):
        """Makes a PUT request"""
        response = self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload
        )
        return response

    def delete(self, endpoint):
        """Makes a DELETE request"""
        response = self.session.delete(
            f"{self.base_url}{endpoint}"
        )
        return response