#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("Hello, are you my mummy?", "my", 0, 23) == 15
    assert find("You are my sunshine", "moonlight", 0, 18) == -1
    assert find("abcdefghijklmnop", "abd", 0, 16) == -1


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0 , 4 , 8 , 12 ,"
    assert multi_find("Hello, are you my mummy?", "my", 0, 23) == "15 , 21 ,"
    assert multi_find("This is a sentence", "notinsentence", 0, 18) == " , "
    assert multi_find("Wibbley wobbly timey wimey stuff", "ey", 0, 32) == "6 , 19 , 25 ,"
