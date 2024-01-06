import pytest
import requests
from src.helpers.api_requests_wapper import *
from src.constants.api_constants import *
from src.helpers.utilies import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from jsonschema import validate, ValidationError


class TestCreateBooking:

    def test_create_booking_tc1(self):
        booking_response = post_request(URL=APIConstants.create_booking(), AUTH=None, HEADER=common_headers(),
                                        Payload=create_booking_payload(), JSON=False)
        verify_status_code(booking_response, 200)
        verify_response(booking_response.json()["bookingid"])
        booking_id = booking_response.json()["bookingid"]
        print(booking_id)

        # schema validation

        output_response = booking_response.json()
        schema_validate = json_schema()

        try:
            validate(instance=output_response, schema=schema_validate)
        except ValidationError as e:
            print(e.message)

    def test_create_booking_tc2(self):
        booking_response = post_request(URL=APIConstants.create_booking(), AUTH=None, HEADER=common_headers(),
                                        Payload=None, JSON=False)
        verify_status_code(booking_response, 500)
