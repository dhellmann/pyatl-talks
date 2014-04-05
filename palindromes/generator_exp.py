#!/usr/bin/env python

import timeit


def longest_palindrome(words):
    return max((w for w in words if w == w[::-1]),
               key=len)


def read_words():
    return open('/usr/share/dict/words', 'r').read().split()


if __name__ == '__main__':
    t = timeit.Timer(
        "longest_palindrome(words)",
        """
from generator_exp import read_words, longest_palindrome
words = read_words()
""",
    )
    print t.timeit(5)
