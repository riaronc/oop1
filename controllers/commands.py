from models.core_classes import Stack


def parse_data(data: list[dict], class_) -> Stack:
    res = Stack[class_]()
    for g in data:
        a = class_(**g)
        res.push(a)
    return res
