#!/usr/bin/env python


def get_file(file_name: str) -> list:
    file = open(file_name, 'r')
    chart = []
    for line in file:
        chart.append(line.replace('\n', ''))
    return chart


def get_collisions(chart: list, right: int, down: int) -> int:
    x = 0
    y = 0
    collisions = 0
    while x < len(chart):
        # Extends chart if needed
        original = chart[x]
        while len(chart[x]) < y:
            chart[x] += original
        chart[x] += original

        if chart[x][y] == '#':
            collisions += 1
        x += down
        y += right
    
    return collisions


def problem_01():
    chart = get_file('input.txt')
    collisions = get_collisions(chart, 3, 1)
    
    print(f"01: {collisions} collisions")


def problem_02():
    chart = get_file('input.txt')

    collisions = []
    collisions.append(get_collisions(chart.copy(), 1, 1))
    collisions.append(get_collisions(chart.copy(), 3, 1))
    collisions.append(get_collisions(chart.copy(), 5, 1))
    collisions.append(get_collisions(chart.copy(), 7, 1))
    collisions.append(get_collisions(chart.copy(), 1, 2))
    
    answer = 1
    for i in collisions:
        answer *= i

    print(f"02: {collisions} collisions, answer: {answer}")


if __name__ == "__main__":
    problem_01()
    problem_02()


