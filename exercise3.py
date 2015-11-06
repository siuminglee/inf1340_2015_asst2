#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""
from test_exercise3 import GRADUATES, MANAGERS

__author__ = 'Rachel Lee'
__email__ = "siuming.lee@mail.utoronto.ca"



def union(GRADUATES, MANAGERS):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    # return rows that appear in GRADUATES table, but not MANAGERS table
    for row in GRADUATES:
        if row not in MANAGERS:
            return row
    # return rows that appear in MANAGERS table, but not GRADUATES table
    for row in MANAGERS:
        if row not in GRADUATES:
            return row
print union(GRADUATES, MANAGERS)


def intersection(GRADUATES, MANAGERS):
    """
    Describe your function
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    # return rows that appear in both GRADUATES and MANAGERS tables
    for row in GRADUATES:
        if row in MANAGERS:
            return row
        row += 1
print intersection(GRADUATES, MANAGERS)


def difference(GRADUATES, MANAGERS):
    """
    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    # return rows that appear in GRADUATES, but not in MANAGERS table
    for row in GRADUATES:
        if row not in MANAGERS:
            return row
print difference(GRADUATES, MANAGERS)



#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass
