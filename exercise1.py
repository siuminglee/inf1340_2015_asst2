#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Rachel Lee'
__email__ = "siuming.lee@mail.utoronto.ca"
__copyright__ = "2015 Rachel Lee"
__license__ = "n/a"


def pig_latinify(word):
    """
    Describe your function

    :param : word: the word to be converted to pig latin
    :param : vowels: list containing all vowels
    :return: word argument converted into pig latin

    """
    # convert word to lowercase string
    word = str(word.lower())
    # assign a,e,i,o,u to a list called vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # If first letter is a vowel, print word+yay
    index = 0
    if word[0] in vowels:
        word += 'yay'
        return word
    # If first letter is not a vowel, remove all consonants before the first vowel
    # Add those to the end of the word, and append "ay"
    else:
        while word[0] not in vowels:
            word = word[1:] + word[0]
            index += 1
        word += 'ay'
        return word

print (pig_latinify("whisper"))















