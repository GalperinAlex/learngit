def list_max(my_lst):
    max_num = my_lst[0]
    second_big = my_lst[1]
    for num in my_lst:
        if second_big > num < max_num:
            second_big = num
        else:
            max_num = num
    return second_big

l1 = [1, 15, 25, 30, 60, 99]
max1 = list_max(l1)

l2 = [22, 54, 66, 53, 333, 9]
max2 = list_max(l2)

print(max1, max2)
max_l = [max1, max2]

#max = list_max(max_l)
#print(max)
