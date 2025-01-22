# it prevent some errors in your program or code
try:
    x = int(input('Input an interger: '))
    print(x)
except:
    print('Value not an interger')  

    #
try:
    x = int(input('Input an interger: '))
    print(x)
except:
    print('something went wrong')    
else:
    print('nothing went wrong')   
    # 
try:
    x = int(input('Input an interger: '))
    print(x)
except:
    print('something went wrong')    
finally:
    print('try except finished')     