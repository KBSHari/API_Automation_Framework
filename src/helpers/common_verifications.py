def verify_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expected status code is " + str(expected_data)


def verify_response(key):
    assert key is not None, "Response is null"
