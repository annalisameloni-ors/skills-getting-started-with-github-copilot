"""
Test GET /activities and GET / endpoints using AAA (Arrange-Act-Assert) pattern.
"""

def test_get_activities(client):
    # Arrange: (client fixture provides TestClient)
    
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    for activity, details in data.items():
        assert "description" in details
        assert "schedule" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)

def test_root_redirects(client):
    # Arrange
    # (client fixture provides TestClient)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (302, 307)
    assert "/static/index.html" in response.headers.get("location", "")
