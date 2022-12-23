#Declaring Functions
def input_deg()->int:   #Functions for inputting degree
    cnt = 0
    while(cnt < 3):
        cnt += 1
        try:
            deg = int(input('Please enter the degree: ').strip())
        except Exception:
            print('Degree should be non-negative integer not greater than 3')
            continue
        if(deg in range(0, 4)):
            return deg
    return -1

def input_coeff(num:int)->float:  #Functions for inputting coefficients
    cnt = 0
    string = 'Please input Coefficient %i: ' %num
    while(cnt < 3):
        cnt += 1
        try:
            coeff = float(input(string).strip())
        except Exception:
            print('Coefficient should be real number')
            continue
        if((num == 1) and (coeff == 0)):
            print('The leading coefficient cannot be 0')
            continue
        return coeff
    return False

def input_bounds(flag:bool)->float: #Function for inputting upper and lower bounds
    cnt = 0
    if(flag):
        string = 'Please enter the upper bound: '
    else:
        string = 'Please enter the lower bound: '
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input(string).strip())
        except:
            print('Please enter a real number')
            continue
        return inpt
    return False

def input_step(upper_bound:float, lower_bound:float)->int:  #Function to input the step
    cnt = 0
    while(cnt < 3):
        cnt += 1
        try:
            inpt = int(input('Please provide the value of step to increment: ').strip())
        except:
            print('Please enter an integer')
            continue
        if(inpt > 0):
            if((upper_bound - lower_bound)%inpt < 0.01):
                return inpt
            else:
                print('Enter an appropriate values for given bounds.')
        else:
            print('Value of step should be greater than 0')
    return -1

def output_val(val:int, coefficients:list)->int:   #Function to find values
    count = 0
    deg = len(coefficients) - 1
    for idx, coeff in enumerate(coefficients):
        power = deg - idx
        count += pow(val, power)*coeff
    count = int(round(count))   #If answer is not integer, round it
    return count

def print_output(nums:list):    #Function to print the values (had to add because (-)ve integers)
    min_num = min(nums)
    min_num = abs(min(min_num, 0))
    for num in nums:
        print(' '*(min(min_num + num, min_num)) + '*'*abs(num))
    return

def main():
    print('Please provide the details of the polynomial:-')
    degree = input_deg()
    if(degree == -1):
        print('Program terminated due to multiple invalid inputs')
        return
    coeffecients = list()
    for i in range(1, degree + 2):
        coeff = input_coeff(i)
        if(coeff is False):
            print('Program terminated due to multiple invalid inputs')
            return
        coeffecients.append(coeff)
    lower_bound = input_bounds(False)
    if(lower_bound is False):
        print('Program terminated due to multiple invalid inputs')
        return
    upper_bound = input_bounds(True)
    if(upper_bound == 'False'):
        print('Program terminated due to multiple invalid inputs')
        return
    if(lower_bound >= upper_bound):
        print('The upper bound must be greater than lower bound')
        return
    step = input_step(upper_bound, lower_bound)
    if(step == -1):
        print('Program terminated due to multiple invalid inputs')
        return
    print('The value of function between %.2f and %.2f is:' %(lower_bound, upper_bound))
    output_list = list()
    num = lower_bound
    while num <= upper_bound:
        output_list.append(output_val(num, coeffecients))
        num += step
    print_output(output_list)
    return

#Driver Code
print('-'*60)
main()
print('-'*60)