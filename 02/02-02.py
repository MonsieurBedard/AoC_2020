#!/usr/bin/env python

file = open('input.txt', 'r')

correct = 0

for line in file:
    array = line.replace('-', ' ').split()
    positions = []
    positions.append(int(array[0]))
    positions.append(int(array[1]))
    character = array[2].replace(':', '')
    password = array[3]

    count = 0
    
    for p in positions:
        if password[p - 1] == character:
            count += 1

    if count == 1:
        correct += 1

print(correct)