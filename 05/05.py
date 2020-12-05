#!/usr/bin/env python

import os


def get_file(file_name: str):
    fn = os.path.join(os.path.dirname(__file__), file_name)
    file = open(fn, 'r')
    data = []
    for line in file:
        data.append(line)
    return data


def get_seat(boarding_pass: str):
    upper = 127
    lower = 0
    for i in range(7):
        char = boarding_pass[i]
        if char == 'F':
            val = ((upper + lower) / 2) - 0.5
            upper = val
        elif char == 'B':
            val = ((upper + lower) / 2) + 0.5
            lower = val
    row = int(upper)

    upper = 7
    lower = 0
    for i in range(3):
        char = boarding_pass[i + 7]
        if char == 'L':
            val = ((upper + lower) / 2) - 0.5
            upper = val
        elif char == 'R':
            val = ((upper + lower) / 2) + 0.5
            lower = val
    col = int(upper)

    seat_id = int(row * 8 + col)

    return row, col, seat_id


def answer_01():
    boarding_passes = get_file('input.txt')

    highest = 0
    for boarding_pass in boarding_passes:
        row, col, seat_id = get_seat(boarding_pass)
        if seat_id > highest:
            highest = seat_id
    print(f"Highest seat_id = {highest}")


def answer_02():
    boarding_passes = get_file('input.txt')

    highest = 0
    seat_ids = []
    for boarding_pass in boarding_passes:
        row, col, seat_id = get_seat(boarding_pass)
        seat_ids.append(seat_id)
        if seat_id > highest:
            highest = seat_id
    for i in range(highest):
        if i - 1 in seat_ids and i + 1 in seat_ids and i not in seat_ids:
            print(f"my seat_id = {i}")


if __name__ == "__main__":
    answer_01()
    answer_02()
