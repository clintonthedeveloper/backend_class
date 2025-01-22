list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'mangoes', 'oranges', 'apples', 'watermelone']
list2.extend(list2)
# insert
list2.insert(1, 'cherry')
list2.clear()
print(list2.index('mango'))
print(list1)
