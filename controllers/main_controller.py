import json


def create_new_entity(entity, class_) -> None:
    print(f"Provide data inb JSON format to create a new {class_.__name__}:")
    input_data = input()
    is_json_ = False
    created = False
    while not is_json_ and not created:
        try:
            data = json.loads(input_data)
            is_json_ = True
            a = class_(**data)
            entity.add(a)
            created = True
        except Exception:
            print("Bad input data format. Try again")
            input_data = input()
    print("Successfully created new object")
    return


def delete_selected_entity(entity) -> None:
    print("Print ID of entity to delete:")
    id_ = input()
    while not id_.isalnum():
        print("Print ID of entity to delete:")
    ent = entity.delete(id_)
    print(f"Successfully deleted: {ent}")
    return


def find_selected_entity(entity) -> None:
    print("Print ID of entity to find:")
    id_ = input()
    while not id_.isalnum():
        print("Print ID of entity to find:")
    ent = entity.delete(id_)
    print(ent)
    return
