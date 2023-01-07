from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    print({"status_code": response.status_code,
          "response.json()": response.json()})
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
