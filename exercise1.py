#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Rachel Lee'
__email__ = "siuming.lee@mail.utoronto.ca"
__copyright__ = "2015 Rachel Lee"
__license__ = "n/a"



word = raw_input("Enter a word: ")

#assign a,e,i,o,u to a list called vowels
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

character = 0
for letter in word:
    if letter[0] in vowels:
        print word + 'ay'
    else:
        if letter[0] in consonants:
            print word[1:] + word[0] + "yay"
        character += 1













