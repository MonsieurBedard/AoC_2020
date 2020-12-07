#!/usr/bin/env python

import os


FILE_NAME = 'input.txt'


def answer_01():
    fn = os.path.join(os.path.dirname(__file__), FILE_NAME)
    with open(fn, 'r') as file:
        data = file.read().split('\n\n')
        for i in range(len(data)):
            data[i] = data[i].replace('\n', '')
            data[i] = ''.join(set(data[i]))

    total = 0
    for d in data:
        total += len(d)

    print(f'Answer 01 = {total}')


def answer_02():
    fn = os.path.join(os.path.dirname(__file__), FILE_NAME)
    with open(fn, 'r') as file:
        data = file.read().split('\n\n')
        for i in range(len(data)):
            data[i] = data[i].split('\n')

    total = 0
    for i in range(len(data)):
        chars = data[i][0]
        for char in chars:
            inside = True
            for dd in data[i]:
                if char not in dd:
                    inside = False
            if inside:
                total += 1

    print(f'Answer 02 = {total}')


if __name__ == "__main__":
    answer_01()
    answer_02()
