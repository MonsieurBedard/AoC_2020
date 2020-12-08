#!/usr/bin/env python

import os


FILE_NAME = 'input.txt'


def get_data():
    fn = os.path.join(os.path.dirname(__file__), FILE_NAME)
    data = []
    with open(fn, 'r') as file:
        for line in file:
            line = line.split(' ')
            name = line[0]
            value = int(line[1])
            data.append([name, value])
    return data


def answer_01():
    data = get_data()

    acc = 0
    idx = 0
    index_list = []
    while idx != len(data):
        instruction = data[idx][0]
        value = data[idx][1]

        if idx not in index_list:
            index_list.append(idx)
        else:
            break

        if instruction == 'nop':
            idx += 1
        elif instruction == 'acc':
            acc += value
            idx += 1
        elif instruction == 'jmp':
            idx += value

    print(f"answer 01 = {acc}")


def answer_02():
    data = get_data()

    acc = 0

    # brute force is the best kind of force
    for i in range(len(data)):
        data = get_data()

        if data[i][0] == 'jmp':
            data[i][0] = 'nop'
        elif data[i][0] == 'nop':
            data[i][0] = 'jmp'

        acc = 0
        idx = 0
        completable = True
        index_list = []
        while idx != len(data) and completable == True:
            instruction = data[idx][0]
            value = data[idx][1]

            if idx not in index_list:
                index_list.append(idx)
            else:
                completable = False

            if instruction == 'nop':
                idx += 1
            elif instruction == 'acc':
                acc += value
                idx += 1
            elif instruction == 'jmp':
                idx += value

        if (idx == len(data)):
            break

    print(f"answer 02 = {acc}")


if __name__ == "__main__":
    answer_01()
    answer_02()
