#Declaring Functions
exponents = []  #Making list of exponents global variable

def custom_inpt_exp(num:int)->float: #Function for inputting the exponents
    cnt = 0
    string = 'Please enter the exponent of %i term: ' %num
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input(string).strip())
            return inpt
        except:
            print('Please enter a real number')
            continue
    print('Program terminated due to multiple invalid inputs')
    return False

def custom_inpt_len()->int: #Function for inputting no. of terms
    cnt = 0
    while(cnt < 3):
        cnt += 1
        try:
            inpt = int(input('Please enter the no. of terms of the polynomial: ').strip())
        except:
            print('Please enter an integer')
            continue
        if(inpt > 0):
            return inpt
        print('Please enter an integer greater than 0')
    print('Program terminated due to multiple invalid inputs')
    return -1

def custom_inpt_bounds(flag:bool, *arg)->float:    #Function to take input for a, b and d
    cnt = 0
    if flag:
        string = 'Please enter the step value: '
    else:
        string = 'Please enter the value of bound: '
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input(string).strip())
        except:
            print('Please enter a real number')
            continue
        if(flag):
            if((inpt > 0) and ((arg[1] - arg[0])%inpt < 0.01)):
                return inpt
            else:
                print('Please enter a valid step value for %.2f and %.2f' %(arg[0], arg[1]))
        else:
            return inpt
    print('Program terminated due to multiple invalid inputs')
    return False

def function(x:float)->float: #To find the value of function inputted at x
    val = 0
    for exp in exponents:
        try:
            val += pow(x, exp) 
        except ZeroDivisionError:
            return False   #Return false if diverges
    return val

def term_approx(a:float, d:float)->float:
    t1 = function(a)
    t2 = function(a + d/2)
    t3 = function(a + d)
    if((t1 is False) or (t2 is False) or (t3 is False)):
        return False
    return (d*(t1 + 4*t2 + t3))/6

def calculate_area(a:float, b:float, d:float)->float:
    area = 0
    lower_limit = a
    while lower_limit < b:
        add = term_approx(lower_limit, d)
        if add is False:
            return False
        area += add
        lower_limit += d
    return area

def main():
    terms = custom_inpt_len()
    if terms == -1:
        return
    for itr in range(terms):
        exp = custom_inpt_exp(itr + 1)
        if exp is False:
            return
        exponents.append(exp)
    exponents.sort(reverse = True)
    a = custom_inpt_bounds(False)
    if(a is False):
        return
    b = custom_inpt_bounds(False)
    if(b is False):
        return
    if(b == a):
        print('Lower and upper bounds must be different')
        return
    if(b < a):
        a, b = b, a
    d = custom_inpt_bounds(True, a, b)
    if(d is False):
        return
    print()
    area = calculate_area(a, b, d)
    if isinstance(area, complex):
        print('The functions attains complex values')
        return
    if area is False:
        print('The function diverges between given limits')
        return
    print('The area of the given polynomial from %.2f to %.2f is %.4f' %(a, b, area))

#Driver Code
print('-'*60)
main()
print('-'*60)