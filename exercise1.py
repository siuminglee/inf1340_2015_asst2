#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



def pig_latinify():

    #assign a,e,i,o,u to a list called vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    print (input('Enter a word'))
    word = input()

    if word[0] in vowels:
        return word + 'hay'
    else:
        while word[0] not in vowels:
            print 'x'

pig_latinify()





