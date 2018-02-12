my_tuple = (1, 2, 3)
# ponizsze nie dziala!
# my_tuple[1] = 5
still_tuple = (4, 5, 6, [7, 8])
still_tuple[-1].append(9)
print(still_tuple)

my_tuple = my_tuple + (4,)
print(my_tuple)