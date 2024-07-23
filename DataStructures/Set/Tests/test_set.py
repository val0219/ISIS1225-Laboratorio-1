from DataStructures.Set import set as set


def setup_tests():
    return set.new_set()


def test_new_set_is_empty():
    s = setup_tests()
    assert set.size(s) == 0
    assert set.is_empty(s)


def test_add_element():
    s = setup_tests()
    s = set.add_element(s, "element")
    assert set.size(s) == 1
    assert not set.is_empty(s)

    s = set.add_element(s, "element")
    assert set.size(s) == 1
    assert not set.is_empty(s)

    s = set.add_element(s, "element2")
    assert set.size(s) == 2
    assert not set.is_empty(s)


def test_remove_element():
    s = setup_tests()
    s = set.add_element(s, "element")
    s = set.add_element(s, "element2")
    s = set.remove_element(s, "element")
    assert set.size(s) == 1
    assert not set.is_empty(s)

    s = set.remove_element(s, "element")
    assert set.size(s) == 1
    assert not set.is_empty(s)

    s = set.remove_element(s, "element2")
    assert set.size(s) == 0
    assert set.is_empty(s)


def test_size():
    s = setup_tests()
    s = set.add_element(s, "element")
    s = set.add_element(s, "element2")
    assert set.size(s) == 2
    assert not set.is_empty(s)


def test_is_empty():
    s = setup_tests()
    assert set.is_empty(s)

    s = set.add_element(s, "element")
    assert not set.is_empty(s)
    assert set.size(s) == 1
