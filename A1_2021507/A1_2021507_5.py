#Declaring Functions
def custom_input(is_menu:bool)->int:    #Function to take input
    cnt = 0
    if(is_menu):
        string = 'Please enter the number of your choice: '
    else:
        string = 'Please enter the integer: '
    while(cnt < 3):
        cnt += 1
        try:
            inpt = int(input(string).strip())
        except Exception:
            print('Please enter an integer')
            continue
        if(inpt >= 0):
            if(is_menu):
                if((inpt > 0) and (inpt < 6)):
                    return inpt
                else:
                    print('Enter a valid choice')
            else:
                return inpt
        else:
            print('The integer cannot be negative')
    return -1

def getReverse(n:int)->int:     #Any trailing/leading zeroes are removed
    return int(str(n)[::-1])

def checkPalindrome(n:int)->bool:   
    n = str(n)
    for i in range(len(n)//2):
        if(n[i] != n[len(n) - i -1]):
            return False
    return True

def checkNarcissistic(n:int)->bool:
    tot = 0
    power = len(str(n))
    m = n
    while(m):
        tot += pow(m%10, power)
        m //= 10
    if(tot == n):
        return True
    return False

def findDigitSum(n:int)->int:
    tot = 0
    while(n):
        tot += n%10
        n //= 10
    if(tot < 10):
        return tot
    else:
        return findDigitSum(tot)

def findSquareDigitSum(n:int)->int:
    tot = 0
    while(n):
        tot += pow(n%10, 2)
        n //= 10
    if tot < 10:
        return tot
    else:
        return tot + findSquareDigitSum(tot)


#Driver Code
options = ['Reverse a number', 'Check if a number is Palindrome', 'Check if number is a Narcissistic Number', 'Find sum of digits', 'Find sum of sqaure of digits', 'Exit']
print('-'*60)
print('Please choose an option:-')
for num, func in enumerate(options):
    print('%i) %s' %(num + 1, func))
print()
inpt = custom_input(True)
if(inpt == -1):
    print('Program Terminated due to multiple invalid inputs')
else:
    num = custom_input(False)
    if(num == -1):
        print('Program Terminated due to multiple invalid inputs')
    else:
        if(inpt == 1):
            print('The reverse of %i is %i' %(num, getReverse(num)))
        elif(inpt == 2):
            if(checkPalindrome(num)):
                print('%i is a Palindrome' %num)
            else:
                print('%i is not a Palindrome' %num)
        elif(inpt == 3):
            if(checkNarcissistic(num)):
                print('%i is a Narcissistic number' %num)
            else:
                print('%i is not a Narcissistic number' %num)
        elif(inpt == 4):
            print('The digital sum of %i is %i' %(num, findDigitSum(num))) 
        elif(inpt == 5):
            print('The sum of squares of digits of %i is %i' %(num, findSquareDigitSum(num)))
        elif(inpt == 6):
            print('The program has been terminated.')
        else:
            print('Invalid Input')               
print('-'*60)



