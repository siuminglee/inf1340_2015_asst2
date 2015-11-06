#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Rachel Lee'
__email__ = "siuming.lee@mail.utoronto.ca"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param input_string : list to be searched
    :param substring : string you are searching for
    :return: lowest index where substring is found in input_string
                if substring is not found in input_string, returns -1
    :raises:

    """

    substring = str(substring)
    input_string = str(input_string)

    if substring in input_string:
        for index in range(len(input_string)):
            if input_string[index:index+len(substring)] == substring[0:]:
                return index
    else:
        return -1

print find("Hello, are you my mummy?", "my", 0, 23)


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param input_string : list to be searched
    :param substring : string you are searching for
    :return: a string with zero or more indices separated by commas
    :raises:

    """
    substring = str(substring)
    input_string = str(input_string)

    for index in range(len(input_string)):
        if input_string[index:index+len(substring)] == substring:
            print index, ",",
            index += 1

multi_find("Hello, are you my mummy?", "my", 0, 23)