from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/users/")
    print({"status_code": response.status_code,
          "response.json()": response.json()})
    assert response.status_code == 200
    assert response.json() == [{'email': 'string', 'id': 1, 'is_active': True, 'items': []},
                               {'email': 'strissssssssng', 'id': 2, 'is_active': True, 'items': []}]
