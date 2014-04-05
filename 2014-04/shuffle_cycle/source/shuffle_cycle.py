#!/usr/bin/env python

import random


def shuffle_cycle(input):
    input = list(input)
    while True:
        random.shuffle(input)
        for s in input:
            yield s


if __name__ == '__main__':
    original = 'abc'
    sc = zip(range(10), shuffle_cycle(original))
    for i, v in sc:
        print v
