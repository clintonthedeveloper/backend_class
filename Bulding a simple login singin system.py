print('Create an Account now')
username = input('Enter user name: ')
password = input('Enter password:')


print('Your account has been created succefully')
print('Login now!')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('Login successfully')
else:
    print('Invalied credentials')    