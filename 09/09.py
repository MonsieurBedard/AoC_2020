#!/usr/bin/env python

import os


FILE_NAME = "input.txt"


def get_data():
    fn = os.path.join(os.path.dirname(__file__), FILE_NAME)
    data = []
    with open(fn, 'r') as file:
        for line in file:
            data.append(int(line))
    return data


def answer_01():
    numbers = get_data()

    answer = 0
    for i in range(25, len(numbers)):
        preamble = numbers[i-25:i]
        possibilities = [x + y for x in preamble for y in preamble]

        if numbers[i] not in possibilities:
            answer = numbers[i]
            break

    print(f"Answer 01 = {answer}")


def answer_02():
    numbers = get_data()

    invalid = 0
    idx = 0
    for i in range(25, len(numbers)):
        preamble = numbers[i-25:i]
        possibilities = [x + y for x in preamble for y in preamble]

        if numbers[i] not in possibilities:
            invalid = numbers[i]
            idx = i
            break

    answer = 0
    for i in range(idx):
        check = 0
        rang = []
        for ii in range(i, idx):
            check += numbers[ii]
            rang.append(numbers[ii])

            if check == invalid:
                answer = min(rang) + max(rang)
                break

    print(f"Answer 02 = {answer}")


if __name__ == "__main__":
    answer_01()
    answer_02()
