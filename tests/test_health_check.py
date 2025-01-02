import allure
import pytest
import requests
import conftest

@allure.feature("Test Ping")
@allure.story("Test connection")
def test_ping(api_client):
    status_code =api_client.ping()
    assert status_code == 201, f"Expected status 201 but got {status_code}"

@allure.feature('Test Ping')
@allure.story('Test server unavailability')
def test_ping_server_unavailable (api_client, mocker):
    mocker.patch.object (api_client.sessions, 'get', side_effect=Exception("Server unavailable"))
    with pytest.raises (Exception, match="Server unavailable"):
        api_client.ping()

@allure.feature('Test Ping')
@allure.story ('Test wrong HTTP method')
def test_ping_wrong_method (api_client, mocker):
    mock_response = mocker. Mock()
    mock_response.status_code = 405
    mocker.patch.object(api_client.sessions, 'get', return_value=mock_response)
    with pytest.raises (AssertionError, match="Expected status 201 but got 405"):
        api_client.ping()

@allure.feature('Test Ping')
@allure.story ('Test wrong Url')
def test_ping_wrong_method (api_client, mocker):
    mock_response = mocker. Mock()
    mock_response.status_code = 404
    mocker.patch.object(api_client.sessions, 'get', return_value=mock_response)
    with pytest.raises (AssertionError, match="Expected status 201 but got 404"):
        api_client.ping()

@allure.feature('Test Ping')
@allure.story ('Test server error')
def test_ping_wrong_method (api_client, mocker):
    mock_response = mocker. Mock()
    mock_response.status_code = 500
    mocker.patch.object(api_client.sessions, 'get', return_value=mock_response)
    with pytest.raises (AssertionError, match="Expected status 201 but got 500"):
        api_client.ping()

@allure.feature('Test Ping')
@allure.story('Test timeout')
def test_ping_timeout(api_client, mocker):
    mocker.patch.object (api_client.sessions, 'get', side_effect=requests.Timeout)
    with pytest.raises (requests.Timeout):
        api_client.ping()

@allure.feature("Test booking")
@allure.story("Test status")
def test_create_booking(api_client,generate_random_booking_data):
    data = generate_random_booking_data
    response = api_client.create_booking(booking_data=data)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"