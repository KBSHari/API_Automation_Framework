import requests


def get_request(URL, AUTH, HEADER, JSON):
    response = requests.get(url=URL, auth=AUTH, headers=HEADER, json=JSON)
    if JSON is True:
        return response.json()
    return response


def post_request(URL, AUTH, HEADER, JSON, Payload):
    response = requests.post(url=URL, auth=AUTH, headers=HEADER, json=Payload)
    if JSON is True:
        return response.json()
    return response


def put_request(URL, AUTH, HEADER, JSON, Payload):
    response = requests.put(url=URL, auth=AUTH, headers=HEADER, json=Payload)
    if JSON is True:
        return response.json()
    return response


def patch_request(URL, AUTH, HEADER, JSON, Payload):
    response = requests.patch(url=URL, auth=AUTH, headers=HEADER, json=Payload)
    if JSON is True:
        return response.json()
    return response


def delete_request(URL, AUTH, HEADER, Payload,JSON):
    response = requests.delete(url=URL, auth=AUTH, headers=HEADER, json=Payload)
    if JSON is True:
        return response.json()
    return response
