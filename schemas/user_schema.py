USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email", "address", "phone", "website", "company"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "address": {
            "type": "object",
            "required": ["street", "city", "zipcode"],
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"}
            }
        },
        "company": {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"}
            }
        }
    }
}

USERS_LIST_SCHEMA = {
    "type": "array",
    "items": USER_SCHEMA,
    "minItems": 1
}

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "userId", "title", "body"],
    "properties": {
        "id": {"type": "integer"},
        "userId": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }
}

POSTS_LIST_SCHEMA = {
    "type": "array",
    "items": POST_SCHEMA,
    "minItems": 1
}