from collections import defaultdict, Counter
# the bad way
text = 'ala ma kota, kot ma ale'
my_dict = dict()

for char in text:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

print(my_dict)

# the better way
my_dict2 = defaultdict(int)
for char in text:
    my_dict2[char] += 1

print(my_dict2 == my_dict)

# the even better way
print(Counter(text))

# the best yet not real :(

def test_counter():
    pass