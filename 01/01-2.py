#!/usr/bin/env python

num_array = []

with open('./input.txt', 'r') as file:
    for line in file:
        num_array.append(int(line))

answer = 0
for i in num_array:
    for j in num_array:
        for h in num_array:
            if i + j + h == 2020:
                answer = i * j * h

print(answer)