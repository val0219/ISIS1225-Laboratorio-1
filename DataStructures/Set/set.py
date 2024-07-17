def new_set():
    my_new_set = {
        'size': 0,
        'elements': set([])
    }
    return my_new_set


def add_element(my_set, element):
    if element not in my_set['elements']:
        my_set['elements'].add(element)
        my_set['size'] += 1
    return my_set


def remove_element(my_set, element):
    if element in my_set['elements']:
        my_set['elements'].remove(element)
        my_set['size'] -= 1
    return my_set


def size(my_set):
    return my_set['size']


def is_empty(my_set):
    return my_set['size'] == 0
