from app import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 500
    assert response.get_json()["message"] == "NEXUS CI/CD Experiment 9 application is running"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 500
    assert response.get_json()["status"] == "healthy"
