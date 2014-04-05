#!/usr/bin/env python

import timeit


def longest_palindrome(words):
    p = set(w for w in words if w == w[::-1])
    return max(p, key=len)


def read_words():
    return open('/usr/share/dict/words', 'r').read().split()


if __name__ == '__main__':
    t = timeit.Timer(
        "longest_palindrome(words)",
        """
from simple_perf import read_words, longest_palindrome
words = read_words()
""",
    )
    print t.timeit(5)
