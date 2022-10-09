from fastapi.testclient import TestClient
from stuart.api import api

client = TestClient(api)

def test_create_event_via_api():
    response = client.post(
        "/stuart",
        json={
            "max_capacity": "45",
            "capacity_required": "10",
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["max_capacity"] == "45"
    assert result["capacity_required"] == "10"

def test_list_events():
    response = client.get("/stuart")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 0