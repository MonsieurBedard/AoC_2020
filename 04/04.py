#!/usr/bin/env python

import os
import re


def get_file(file_name: str):
    fn = os.path.join(os.path.dirname(__file__), file_name)
    return open(fn, 'r')


def create_passports(file):
    passports = []
    data = []
    for line in file:
        if line != '\n':
            line = line.replace('\n', ' ')
            line = line.split()
            data += line
        else:
            passports.append(data)
            data = []
    passports.append(data)
    data = []
    return passports


def check_fields(passport):
    valid = True
    matches = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for match in matches:
        is_in = any(match in p for p in passport)
        if is_in is False:
            valid = False
    return valid


def check_if_valid(passport):
    if check_fields(passport):
        is_valid = True
        for field in passport:
            key = field.split(':')[0]
            value = field.split(':')[1]

            if 'byr' == key:
                num = int(value)
                if not (1920 <= num <= 2002):
                    is_valid = False

            elif 'iyr' == key:
                num = int(value)
                if not (2010 <= num <= 2020):
                    is_valid = False

            elif 'eyr' == key:
                num = int(value)
                if not (2020 <= num <= 2030):
                    is_valid = False

            elif 'hgt' == key:
                num = int(''.join([i for i in value if i.isdigit()]))
                text = ''.join([i for i in value if not i.isdigit()])
                if text == 'cm':
                    if not (150 <= num <= 193):
                        is_valid = False
                elif text == 'in':
                    if not (59 <= num <= 76):
                        is_valid = False
                else:
                    is_valid = False

            elif 'hcl' == key:
                regexp = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
                if not regexp.search(value):
                    is_valid = False

            elif 'ecl' in key:
                matches = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                valid = False
                for match in matches:
                    if value == match:
                        valid = True
                if not valid:
                    is_valid = False

            elif 'pid' == key:
                if len(value) != 9:
                    is_valid = False
                if not value.isdigit():
                    is_valid = False
        
        return is_valid
    else:
        return False


def answer_01():
    file = get_file('input.txt')
    passports = create_passports(file)

    count = 0
    for passport in passports:
        if check_fields(passport):
            count += 1

    print(f'answer_01 = {count}')



def answer_02():
    file = get_file('input.txt')
    passports = create_passports(file)

    count = 0
    for passport in passports:
        if check_if_valid(passport):
            count += 1

    print(f'answer_02 = {count}')


if __name__ == "__main__":
    answer_01()
    answer_02()

