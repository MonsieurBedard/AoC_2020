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


def check_byr(value):
    num = int(value)
    if not (1920 <= num <= 2002):
        return False
    return True


def check_iyr(value):
    num = int(value)
    if not (2010 <= num <= 2020):
        return False
    return True


def check_eyr(value):
    num = int(value)
    if not (2020 <= num <= 2030):
        return False
    return True


def check_hgt(value):
    num = int(''.join([i for i in value if i.isdigit()]))
    text = ''.join([i for i in value if not i.isdigit()])
    if text == 'cm':
        if not (150 <= num <= 193):
            return False
    elif text == 'in':
        if not (59 <= num <= 76):
            return False
    else:
        return False
    return True


def check_hcl(value):
    regexp = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
    if not regexp.search(value):
        return False
    return True


def check_ecl(value):
    matches = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid = False
    for match in matches:
        if value == match:
            valid = True
    if not valid:
        return False
    return True


def check_pid(value):
    if len(value) != 9:
        return False
    if not value.isdigit():
        return False
    return True


def check_if_valid(passport):
    if check_fields(passport):
        checks = []
        for field in passport:
            key = field.split(':')[0]
            value = field.split(':')[1]

            if 'byr' == key:
                checks.append(check_byr(value))
            elif 'iyr' == key:
                checks.append(check_iyr(value))
            elif 'eyr' == key:
                checks.append(check_eyr(value))
            elif 'hgt' == key:
                checks.append(check_hgt(value))
            elif 'hcl' == key:
                checks.append(check_hcl(value))
            elif 'ecl' == key:
                checks.append(check_ecl(value))
            elif 'pid' == key:
                checks.append(check_pid(value))
        
        return False not in checks
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

