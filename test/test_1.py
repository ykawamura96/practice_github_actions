import os


def test_a():
    val = None
    if val == None:  # invalid syntax
        print("")
    assert 1 == 1


def test_b():
    assert 1 == 2


def test_check_dir_structure():
    for d in os.listdir():
        print(d)