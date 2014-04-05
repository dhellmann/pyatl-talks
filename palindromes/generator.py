#!/usr/bin/env python

import timeit


def palindromes(words):
    p = set()
    for w in (i for i in words if i == i[::-1] and i not in p):
        p.add(w)
        yield w


def longest_palindrome(words):
    return max(palindromes(words), key=len)


def read_words():
    return open('/usr/share/dict/words', 'r').read().split()


if __name__ == '__main__':
    t = timeit.Timer(
        "longest_palindrome(words)",
        """
from generator import read_words, longest_palindrome
words = read_words()
""",
    )
    print t.timeit(5)
