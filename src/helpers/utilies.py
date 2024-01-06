# common header & data reader function

def common_headers():
    HEADER_value = {"Content-Type": "application/json"}

    return HEADER_value


def put_request_header(token):
    HEADER_value = {"Content-Type": "application/json",
                    "Accept": "application/json",
                    "Cookie": "token=" + token
                    }

    return HEADER_value


def json_schema():
    validate_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "bookingid": {
                "type": "number"
            },
            "booking": {
                "type": "object",
                "properties": {
                    "firstname": {
                        "type": "string"
                    },
                    "lastname": {
                        "type": "string"
                    },
                    "totalprice": {
                        "type": "number"
                    },
                    "depositpaid": {
                        "type": "boolean"
                    },
                    "bookingdates": {
                        "type": "object",
                        "properties": {
                            "checkin": {
                                "type": "string"
                            },
                            "checkout": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "checkin",
                            "checkout"
                        ]
                    },
                    "additionalneeds": {
                        "type": "string"
                    }
                },
                "required": [
                    "firstname",
                    "lastname",
                    "totalprice",
                    "depositpaid",
                    "bookingdates",
                    "additionalneeds"
                ]
            }
        },
        "required": [
            "bookingid",
            "booking"
        ]
    }

    return validate_schema
