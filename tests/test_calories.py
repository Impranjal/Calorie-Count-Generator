import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.exceptions import DishNotFoundException

client = TestClient(app)


def test_get_calories_dish_not_found(monkeypatch):
    async def mock_process(self, dish_name, servings):
        return None

    monkeypatch.setattr("app.services.calories_calculator.CalorieCalcultor.process", mock_process)

    response = client.post("/get-calories", json={"dish_name": "unknown_dish", "servings": 1})
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_get_calories_invalid_servings():
    response = client.post("/get-calories", json={"dish_name": "chicken biryani", "servings": 0})
    assert response.status_code == 422
    errors = response.json()["detail"]
    assert any("Servings must be a positive integer" in str(e) for e in errors)


    
