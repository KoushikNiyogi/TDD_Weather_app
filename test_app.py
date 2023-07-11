import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_city_weather(client):
    response = client.get('/weather/city/New_York')
    assert response.status_code == 404

    # Add more test cases here for different scenarios

def test_post_city(client):
    response = client.post('/weather/city', json={'city': 'Bengaluru', 'temperature': '25°C','weather' : "Sunny"})
    assert response.status_code == 201

    # Add more test cases here for different scenarios

def test_patch_city(client):
    response = client.patch('/weather/city/New_York', json={'temperature': '22°C'})
    assert response.status_code == 404

    # Add more test cases here for different scenarios

def test_delete_city(client):
    response = client.delete('/weather/city/New_York')
    assert response.status_code == 404

    # Add more test cases here for different scenarios
