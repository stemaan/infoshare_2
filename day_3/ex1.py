# # a = 1
# # b = 2
# # c = 7
# # result = a + b
# # print(result)
# # result = a - b
# # print(result)
# # result = a * 2
# # print(result)
# # result = c / b # 7 / 2
# # print(result, type(result))
# # result = c // b
# # print(result, type(result))
# #
# # z = 4.23
# # print(type(b))
# # print(type(z), z)
# #
# # z_int = int(z)
# # print(type(z_int), z_int)
# #
# # # @TODO: sprawdzic co oznacza ^ w pythonie
# # result = b ^ 4
# # print(result)
# #
# # # print('before', c)
# # # c += 2 # c = c + 2
# # # c -= 5
# # # c *= 4
# # # c /= 6
# # # print('after', c)
# #
# # c = c % 2
# # print(c)
# # zero = 0
# # two = 2
# # print(two / zero)
# #
# # eng = "Tom's house"
# # eng2 = 'Tom\'s house'
# # print(eng)
# text = "Ala ma kota"
# letter_a = text[2]
# last_char = text[-1]
# print(letter_a)
# print(last_char)
# length = len(text)
# print(length)
# # last_char = text[length]
# print(last_char)
# # slices
# something = text[4:8]
# print(something)
# something2 = text[-4:-1]
# print(something2)
# steps = text[0:10:2]
# print(steps)
# dunno = text[0:15]
# #@ todo: adres
# text2 = text[::-1]
# print(text2)
# print(text2.lower())
# #text[0] = 'O'
# print(text)
#
# text = 'O' + text[1:]
# text = text[:4] + 'M' + text[5:]
# print(text)
#@TODO: posprzatac i wyslac!
text3 = "Ala ma kot, kot bardzo lubi Ale"
old = 'kot'
new = 'pies'
count = 1
replaced = text3.replace(old, new, count)
print(text3, id(text3))
print(replaced, id(replaced))