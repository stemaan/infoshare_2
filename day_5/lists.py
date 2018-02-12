# my_list = list(range(0, 11, 2))
# print(my_list)
#
# text = "ala ma kota"
# something = list(text)
# print(something)
# # for element in text:
# #     print(element)
#
# for idx, element in enumerate(something):
#     print(idx, element)
#
# for value in enumerate(something):
#     print(value)
#
# my_list.append(13)
# print(my_list)
#
# my_list.reverse() # IN PLACE
# print(my_list)
#
# my_list2 = reversed(my_list)

#@ TODO: sprwadz czy my_list jest identyczny z my_list2
my_list = list(range(10))
#@ TODO: zrob kopie my_list i przypisz do zmiennej my_list2
my_list2 = my_list.copy() # jeden ze sposobow
#@ TODO: odwroc kolejnosc elementow in place w my_list
my_list.reverse()
#@ TODO: przypisz do zmiennej wynik reversed(my_list2)
#@ TODO: i dokonaj sprawdzenia czy listy sa identyczne
my_list2 = reversed(my_list2) # my_list3 = reversed(my_list2)
print(my_list, my_list2)

if my_list == my_list2:
    print('listy sa takie  same')
else:
    print(id(my_list))
    print(id(my_list2))

print(type(my_list2))

print(isinstance(my_list2, list))
#
# for idx, element in enumerate(my_list2):
#     print(idx, element)

#  wyszukiwanie elemnetow
# print(my_list.index(None))

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.append(list_b)
print(list_a)
print(list_a[3][1])

list_c = [1, [2, 3]]
list_a.extend(list_b)
print(list_a)
list_b.extend(list_c)
print(list_b)

