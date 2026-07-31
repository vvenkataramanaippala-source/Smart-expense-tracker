from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_expense():
    response = client.post("/expenses", json={"title": "Snacks", "amount": 40.0, "category": "Food", "date": "2026-07-31"})
    assert response.status_code == 200

def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200

def test_filter_by_category():
    client.post("/expenses", json={"title": "Bus", "amount": 50.0, "category": "Travel", "date": "2026-07-31"})
    response = client.get("/expenses/filter?category=Travel")
    assert response.status_code == 200

def test_get_total():
    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert "total" in response.json()

def test_delete_expense():
    create_res = client.post("/expenses", json={"title": "Movie", "amount": 200.0, "category": "Entertainment", "date": "2026-07-31"})
    expense_id = create_res.json()["id"]
    response = client.delete(f"/expenses/{expense_id}")
    assert response.status_code == 200