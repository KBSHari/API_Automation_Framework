import pytest
import requests
from src.helpers.api_requests_wapper import *
from src.constants.api_constants import *
from src.helpers.utilies import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *


class TestRestfullBooker:
    @pytest.fixture()
    def create_token(self):
        response = post_request(URL=APIConstants.create_token(), AUTH=None, HEADER=common_headers(),
                                Payload=create_token_payload(), JSON=False)
        token = response.json()["token"]
        return token

    @pytest.fixture()
    def create_booking(self):
        booking_response = post_request(URL=APIConstants.create_booking(), AUTH=None, HEADER=common_headers(),
                                        Payload=create_booking_payload(), JSON=False)
        verify_status_code(booking_response, 200)
        verify_response(booking_response.json()["bookingid"])
        booking_id = booking_response.json()["bookingid"]
        return booking_id

    def test_update_booking(self,create_booking,create_token):
        booking_id = create_booking
        Header_token = create_token
        update_response = put_request(URL=APIConstants.get_put_patch_delete(booking_id), AUTH=None,
                                      HEADER=put_request_header(Header_token),
                                      Payload=update_booking_payload(), JSON=False)

        verify_status_code(update_response,200)
        verify_response(update_response)

    def test_delete_booking(self,create_booking,create_token):
        booking_id = create_booking
        Header_token = create_token
        delete_response = delete_request(URL=APIConstants.get_put_patch_delete(booking_id), AUTH=None,
                                         HEADER=put_request_header(Header_token),
                                         Payload={}, JSON=False)

        verify_status_code(delete_response,201)
        verify_response(delete_response)
