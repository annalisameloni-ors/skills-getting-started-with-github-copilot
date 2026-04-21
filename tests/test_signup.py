"""
Test POST /activities/{activity_name}/signup endpoint using AAA (Arrange-Act-Assert) pattern.
"""
import random
import string
import pytest

def random_email():
    return (
        "testuser_" + ''.join(random.choices(string.ascii_lowercase, k=6)) + "@mergington.edu"
    )

def test_signup_success(client):
    # Arrange
    email = random_email()
    activity = "Chess Club"
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    # Accepts the actual message format from backend
    assert data["message"].lower().startswith("signed up")

def test_signup_duplicate(client):
    # Arrange
    email = random_email()
    activity = "Chess Club"
    client.post(f"/activities/{activity}/signup?email={email}")
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data.get("detail", "")

def test_signup_nonexistent_activity(client):
    # Arrange
    email = random_email()
    activity = "Nonexistent Club"
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data.get("detail", "")
