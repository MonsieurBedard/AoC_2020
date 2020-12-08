#!/usr/bin/env python

import os


FILE_NAME = 'input.txt'


class Bag():
    def __init__(self, input) -> None:
        self.color = input[0]
        self.bags = {}
        for bag in input[1:]:
            key = ''.join([i for i in bag if not i.isdigit()]).lstrip()
            value = [int(i) for i in bag.split() if i.isdigit()]
            self.bags[key] = value


re = {
    '\n': '',
    'bags contain': '-',
    ' bags.': '',
    ' bag.': '',
    'bags,': '-',
    'bag,': '-',
    'bag': '',
}


def get_data():
    fn = os.path.join(os.path.dirname(__file__), FILE_NAME)
    bags = {}
    with open(fn, 'r') as file:
        for line in file:
            for key in re:
                line = line.replace(key, re[key])
            bag = Bag(line.split(' - '))

            bags[bag.color] = bag

    return bags


def check_if_contain(bag, dic):
    contain = False
    if 'no other' not in bag.bags:
        if 'shiny gold' in bag.bags:
            contain = True
        else:
            for b in bag.bags:
                if check_if_contain(dic[b], dic):
                    contain = True
    return contain


def count_bags(bag, dic):
    count = 0
    for b in bag.bags:
        if b != 'no other':
            count += bag.bags[b][0]
            val = bag.bags[b][0]
            for _ in range(val):
                count += count_bags(dic[b], dic)
    return count


def answer_01():
    bags = get_data()

    count = 0
    for bag in bags:
        if check_if_contain(bags[bag], bags):
            count += 1

    print(f'Answer 01 = {count}')


def answer_02():
    bags = get_data()

    count = 0
    count = count_bags(bags['shiny gold'], bags)

    print(f'Answer 02 = {count}')


if __name__ == "__main__":
    answer_01()
    answer_02()
