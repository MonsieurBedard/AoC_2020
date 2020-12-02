#!/usr/bin/env python

file = open('input.txt', 'r')

correct = 0

for line in file:
    array = line.replace('-', ' ').split()
    minimum = int(array[0])
    maximum = int(array[1])
    character = array[2].replace(':', '')
    password = array[3]

    count = 0
    for c in password:
        if c == character:
            count += 1
    
    if minimum <= count and count <= maximum:
        correct += 1

print(correct)