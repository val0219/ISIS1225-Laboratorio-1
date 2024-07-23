import csv


def new_set():
    """Crea un conjunto vacío

    Returns:
        set: Set creado
    """
    my_new_set = {
        'size': 0,
        'elements': []
    }
    return (my_new_set)


def add_element(my_set, element):
    if element not in my_set['elements']:
        my_set['elements'].append(element)
        my_set['size'] += 1
    return my_set


def remove_element(my_set, element):
    if element in my_set['elements']:
        my_set['elements'].remove(element)
        my_set['size'] -= 1
    return my_set


def load_set(my_set, filename):
    if (filename is not None):
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=",")
    for line in input_file:
        add_element(my_set, line)
    return (my_set)


def size(my_set):
    return my_set['size']


def is_empty(my_set):
    return my_set['size'] == 0
