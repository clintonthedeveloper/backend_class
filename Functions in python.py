# functions helps to restracture ypur code well
def greetings_function(name):
    print('welcome'+name)

greetings_function('clinton')

# 
def greetings_function(name):
    print('welcome'+str(name))

greetings_function(34)

# 
def greetings_function(name, age):
    print('welcome' +name+', your are '+str(age)+' years old.')

greetings_function('clinton', 27)

# list of value and you dont know the amount of value your passing out
def greetings_function(*names):
    print('welcome'+names[1])

greetings_function('clinton', 'ochieng', 'lennox')

# 
def greetings_function(name, age):
    print('welcome' +name+', your are '+str(age)+' years old.')

name = input('Enter your name: ')
age = input('enter your age')
greetings_function('clinton', 27)




