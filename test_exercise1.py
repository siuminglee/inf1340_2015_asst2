#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Rachel Lee'
__email__ = "siuming.lee@mail.utoronto.ca"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

    assert pig_latinify("ScaLLywag") == "allywagscay"
    assert pig_latinify("oodles") == "oodlesyay"
    assert pig_latinify("Barley") == "arleybay"
    assert pig_latinify("whisper") == "isperwhay"


