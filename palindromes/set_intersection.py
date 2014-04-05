#!/usr/bin/env python


def find_palindromes(words):
    a = set(words)
    b = set(w[::-1] for w in words)
    c = a.intersection(b)
    return c


if __name__ == '__main__':
    words = open('/usr/share/dict/words', 'r').read().split()
    p = find_palindromes(words)
    print 'Count:', len(p)
    print 'First:', iter(p).next()
    print 'Longest:', max(p, key=len)
