from fastapi.testclient import TestClient
from stuart.api import api

client = TestClient(api)

def test_create_event_via_api():
    response = client.post(
        "/stuart",
        json={
            "max_capacity": "45",
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["max_capacity"] == 45
    assert result["id"] == 1

def test_update_event_via_api():
    response = client.post(
        "/stuart",
        json={
            "max_capacity": "45",
        },
    )
    response = client.put(
        "/update_capacity/1",
        json={
            "max_capacity": "55",
        },
    )
    assert response.status_code == 200
    result = response.json()
    assert result["max_capacity"] == 55
    assert result["id"] == 1

def test_list_events():
    response = client.get("/capacity_required?max_capacity=45")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 0