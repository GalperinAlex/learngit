#!/usr/bin/python

#boom=range(100)
#for num in boom:
#    if (num == % 7):
#       print("7boom")



for num in range(1, 101):
    if num % 7 == 0 or '7' in str(num):
        print("boom")
    else:
        print(num)
