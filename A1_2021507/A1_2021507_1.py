#Declaring functions corresponding to each pattern
def right_triangle(n:int)->bool:
    for i in range(1, n + 1):
        print(' '.join([str(j) for j in range(1, i + 1)]))
    return True

def isosceles_triangle(n:int)->bool:
    if(n&1):
        return False
    for i in range(n):
        print(' '*(2*(n - i - 1)), end = '')
        print(' '.join([str(j) for j in range(1, 2*i + 2)]))
    return True
    
def kite(n:int)->bool:
    if(n&1):
        return False
    for i in range(n):
        print(' '*(2*(n - i - 1)), end = '')
        print(' '.join([str(j) for j in range(1, 2*i + 2)]))
    for i in range(n - 2, -1, -1):
        print(' '*(2*(n - i - 1)), end = '')
        print(' '.join([str(j) for j in range(1, 2*i + 2)]))
    return True

def half_kite(n:int)->bool:
    for i in range(1, n + 1):
        print(' '.join([str(j) for j in range(1, i + 1)]))
    for i in range(n - 1, 0, -1):
        print(' '.join([str(j) for j in range(1, i + 1)]))
    return True

def X(n:int)->bool:
    if(n&1):
        return False
    for i in range(n - 1, 0, -1):
        print(' '*(2*(n - i - 1)), end = '')
        print(' '.join([str(j) for j in range(1, 2*i + 2)]))
    for i in range(n):
        print(' '*(2*(n - i - 1)), end = '')
        print(' '.join([str(j) for j in range(1, 2*i + 2)]))
    return True

#Driver Code
print('-'*60)
print('Welcome to Pattern Generator')
print('Please select one of the following patterns to print:-')
print('1)Right angled triangle')
print('2)Isosceles triangle')
print('3)Kite')
print('4)Half Kite')
print('5)X')
print('To terminate the program please enter \'Exit\'.')
print('-'*60)

cnt = 0     #to count no. of invalid inputs. Program terminates on multiple invalid inputs so user doesn't get stuck in infinite loop.
while True:
    inpt = input("Please enter your choice:- ").strip().lower()

    if(inpt == 'right angled triangle' or inpt == '1'):
        try:
            n = int(input('Please enter the value of n:- ').strip())
        except Exception:
            cnt += 1
            if(cnt == 3):   #If 3 invalid inputs are entered, the program terminates
                print('Program terminated due to multiple invalid inputs.')
                print('-'*60)
                break
            print('Please enter an integer')
            continue
        right_triangle(n)

    elif(inpt == 'isosceles triangle' or inpt == '2'):
        try:
            n = int(input('Please enter the value of n:- ').strip())
        except Exception:
            cnt += 1
            if(cnt == 3):   #If 3 invalid inputs are entered, the program terminates
                print('Program terminated due to multiple invalid inputs.')
                print('-'*60)
                break
            print('Please enter an integer')
            continue
        a = isosceles_triangle(n)
        if(not a):
            print('Please enter a valid value for n.')

    elif(inpt == 'kite' or inpt == '3'):
        try:
            n = int(input('Please enter the value of n:- ').strip())
        except Exception:
            cnt += 1
            if(cnt == 3):   #If 3 invalid inputs are entered, the program terminates
                print('Program terminated due to multiple invalid inputs.')
                print('-'*60)
                break
            print('Please enter an integer')
            continue
        a = kite(n)
        if(not a):
            print('Please enter a valid value for n.')

    elif(inpt == 'half kite' or inpt == '4'):
        try:
            n = int(input('Please enter the value of n:- ').strip())
        except Exception:
            cnt += 1
            if(cnt == 3):   #If 3 invalid inputs are entered, the program terminates
                print('Program terminated due to multiple invalid inputs.')
                print('-'*60)
                break
            print('Please enter an integer')
            continue
        half_kite(n)

    elif(inpt == 'x' or inpt == '5'):
        try:
            n = int(input('Please enter the value of n:- ').strip())
        except Exception:
            cnt += 1
            if(cnt == 3):   #If 3 invalid inputs are entered, the program terminates
                print('Program terminated due to multiple invalid inputs.')
                print('-'*60)
                break
            print('Please enter an integer')
            continue
        a = X(n)
        if(not a):
            print('Please enter a valid value for n.')

    elif(inpt == 'exit'):   #If 'exit' is given as input, the program terminates
        print('Program Terminated')
        print('-'*60)
        break
    
    else:   #incase of invalid input
        cnt += 1
        if(cnt == 3):   #If 3 invalid inputs are entered, the program terminates
            print('Program terminated due to multiple invalid inputs.')
            print('-'*60)
            break
        else:
            print('Please enter a valid input.')
            