import faker
from faker import Faker
from dotenv import load_dotenv
import os

faker = Faker()


def create_booking_payload():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": 111,
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    return payload


def create_token_payload():
    load_dotenv()
    payload = {
        "username": os.getenv("USERNAMEs"),
        "password": os.getenv("PASSWORD")
    }
    return payload


def update_booking_payload():
    payload = {
        "firstname": "Jims_update",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    return payload
