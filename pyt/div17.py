#!/usr/bin/python

min = int(input("please enter min range: "))
max = int(input("please enter max range: "))
for num in range(min,max):
    if (num % 17) == 0: 
        print(num)
        break
else:
    print("no num dividable by 17")
