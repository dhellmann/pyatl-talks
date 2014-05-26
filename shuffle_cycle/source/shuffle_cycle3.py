#!/usr/bin/env python3

import random


def shuffle_cycle(input):
    input = list(input)
    while True:
        random.shuffle(input)
        yield from iter(input)  # removed loop


if __name__ == '__main__':
    original = 'abc'
    sc = list(zip(range(10), shuffle_cycle(original)))  # list
    print(sc)
