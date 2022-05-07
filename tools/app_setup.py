import json
from models.core_classes import Stack


def read_the_file(filename: str):
    with open(filename) as file:
        raw_data = file.read()
        data = json.loads(raw_data)
        return data


def parse_data(data: list[dict], class_) -> Stack:
    res = Stack[class_]()
    for g in data:
        a = class_(**g)
        res.add(a)
    return res
