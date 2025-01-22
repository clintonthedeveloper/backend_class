a = 4
b= 3

if a>b:
    print(str(a) + 'is greater than ' + str(b))

    # 
a = True
b = 'clinton'

if a == True:
    print('a is True')

    # 
a = False
b = 'clinton'

if a != True:
    print('a is not True') 

# 
a = 4
b =4

if a >= b:
    print('True')

    # 
a = 4
b =5

if a == b:
    print('a equal b')
else:
    print('a not equal b')
    # 
    boy = True
    short = True

if boy == True and short == False:
    print('He is a boy or he is short')

else:
    print('A is none of the two')    

#
value = input('Input a value: ')

if type(value) == str:
    print(value + ' is a string')
elif type(value) == int:
    print(value + ' is an integer')    
elif type (value) == list:
    print(value + 'is a list')    
else:
    print('we don\'t know the data type of ' + value)    

# 
value = input('Input a value:')

if (value)== str:
    print(value + 'is a string')
else:
    print(value, ' is not a string ')

# 
value = int(input('Input a number: '))
value: int
if value%5:
    print(value + 'is not a string')
else:
    print(value, 'is not a string')    

    # or
    print(20%5)