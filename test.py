# coding=utf-8
from array import array

# IF

if 1 > 2:
    print('1 > 2')
elif 2 > 3:
    print('2 > 3')
else:
    print('none of')

# Lists
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# lst.remove(3)
#
# lst.append(6)
#
# lst.remove(60)
#
# print(len(lst))
#
# arr = array('i', lst)
#
# print(lst.__sizeof__())
# print(arr.__sizeof__())

# Sets
#
# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 4, 5}
#
# set1.add(1)
#
# set1.remove(1)
#
# print(set1.difference([2, 3]))
# print(set1.intersection(set2))
#
# print(set1)

# hash
# hash("abc") => 50
# hash("cba") => 50
# [ , , , , ,..., "abc", ... ]
# set.remove("abc")
# hash("123")
# [ , , , , ,..., ["abc", "cba"], ... ]

# Dictionary

# [ , , , , ,..., "abc" -> 1, ... ]
#
dct = {'a': 1, 'b': 2}
#
print(dct.get('a'))

# https://github.com/ignatyev/concerts-telegram-bot

@simple_bobot