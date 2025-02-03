question = input('Do you have an account? (Y or N): ').lower()

if question == 'n':
    print('Welcome to the Signup page, Please fill in these details')
    email = input('Enter Your Email: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    password2 = input('Re-Enter Password: ')

    if password == password2:
        print('Your account has been created successfully')
        print('Redirecting to Login Page, Please Wait...')
    else:
        print('Passwords don\'t match, Kindly check for inconsistencies!')
        print('Exiting Program!')
else:
    if question == 'y':
        username2 = input('Enter username: ')
        password2 = input('Enter password: ')

        if username2 == username and password2 == password:
            print('Login successfully')
        else:
            print('Invalid credentials')
    else:
        print('Invalid Input, Try Again!!')


