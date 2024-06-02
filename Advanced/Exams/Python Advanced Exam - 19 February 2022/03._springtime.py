def start_spring(**kwargs):
    objects = {}

    for current_object, type_of_object in kwargs.items():
        if type_of_object not in objects:
            objects[type_of_object] = []
        objects[type_of_object].append(current_object)

    sorted_objects = dict(sorted(objects.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = []

    for key, value in sorted_objects.items():
        result.append(f"{key}:")
        for curr_obj in sorted(value):
            result.append(f"-{curr_obj}")

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower"}

print(start_spring(**example_objects))
