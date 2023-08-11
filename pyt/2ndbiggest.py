#!/usr/bin/python

numbers = [15, 2, -4, 7, 101, 78, 44, 2]

biggest = max(numbers)
secondbig = min(numbers)


for lsnum in numbers:
    if secondbig <  lsnum < biggest:
        secondbig = lsnum
print(secondbig)

