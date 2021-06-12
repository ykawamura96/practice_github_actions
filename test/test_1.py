from os.path import join
import os

WORKING_DIR = join(os.environ['HOME'], 'work',
                   'practice_github_actions', 'practice_github_actions')


def test_a():
    val = None
    if val == None:  # invalid syntax
        print("")
    assert 1 == 1


def test_b():
    assert 1 == 1


def test_check_dir_structure():
    for d in os.listdir():
        print(d)    
    for d in os.listdir(WORKING_DIR):
        print(d)


test_check_dir_structure()