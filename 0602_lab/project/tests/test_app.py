from app import app


def test_home(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.0.1")
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, CI/CD!", "version": "1.0.1"}


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
