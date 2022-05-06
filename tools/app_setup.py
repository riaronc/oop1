import json


def read_the_file(filename: str):
    with open(filename) as file:
        raw_data = file.read()
        data = json.loads(raw_data)
        return data
#
# def poll_events():
#