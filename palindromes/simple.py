#!/usr/bin/env python


def find_palindromes(words):
    return set(w for w in words if w == w[::-1])


if __name__ == '__main__':
    words = open('/usr/share/dict/words', 'r').read().split()
    p = find_palindromes(words)
    print 'Count:', len(p)
    print 'First:', iter(p).next()
    print 'Longest:', max(p, key=len)
