#Declaring functions
def input_cost()->float:
    cnt = 0
    while cnt < 3:
        cnt += 1
        try:
            inpt = float(input('Enter the initial cost of buying the car: ').strip())
        except Exception:
            print('Please enter a number.')
            continue
        if(inpt >= 0):
            return inpt
        print('Please enter a number greater than 0.')
    print('Program terminated due to multiple incorrect inputs.')
    return -1

def input_rate()->float:
    cnt = 0
    while cnt < 3:
        cnt += 1
        try:
            inpt = float(input('Enter the rate of depreciation: ').strip())
        except Exception:
            print('Please enter a number.')
            continue
        if(inpt >= 0) and (inpt <= 100):
            return inpt/100
        print('Please enter a number between 0 and 100.')
    print('Program terminated due to multiple incorrect inputs.')
    return -1

def main():
    init_cost = input_cost()
    if init_cost == -1:
        return
    dep_rate = input_rate()
    if dep_rate == -1:
        return
    value_derived = 6000*50
    maintainance = 0
    print()
    if(init_cost < value_derived):
        print('Initial cost is less than value derived in the first year')
        return
    time = 1
    cost = init_cost
    while(time < 15):
        if(time <= 5):
            maintainance += init_cost/100
        else:
            maintainance *= 1.5
        cost = cost - init_cost*dep_rate - maintainance
        value_derived *= 1.1
        if(cost < value_derived):
            break
        time += 1
    print('The car should be sold after %i years' %time)
    return

#Driver code
print('-'*60)
main()
print('-'*60)