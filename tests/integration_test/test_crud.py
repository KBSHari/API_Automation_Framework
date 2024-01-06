from src.constants.api_constants import APIConstants


def test_urls():
    print(APIConstants.base_url())
    print(APIConstants.create_token())
    print(APIConstants.create_booking())
    print(APIConstants.put_patch_delete(2))