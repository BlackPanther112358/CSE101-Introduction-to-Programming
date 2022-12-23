def input_itemprice(num:int)->float:   #Function for taking input for price
    cnt = 0
    string = 'Enter the price of %i item: ' %(num)
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input(string))
        except:
            print('Please enter a real number greater than 0')
            continue
        if(inpt > 0):
            return inpt
        print('The cost of item cannot be negative')
    print('Program terminated due to multiple incorrect inputs')
    return -1

def input_phnum()->int:     #Function for inputting phone number
    cnt = 0
    while(cnt < 3):
        cnt += 1
        inpt = input('Please enter the your phone number: ')
        if(len(inpt) == 10):
            if(inpt.isdigit()):
                return inpt
            else:
                print('Please enter a valid phone number')
        else:
            print('The phone number must have exactly 10 digits')
    print('Program terminated due to multiple incorrect inputs')
    return -1

def input_discount(num:int)->float:    #Function for inputting discount
    cnt = 0
    string = 'Enter the discount (in percentage) of %i saver combo: ' %(num)
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input(string))
        except:
            print('Please enter a positive number')
            continue
        if((inpt >= 0) and (inpt <= 100)):
            return(1 - inpt/100)
        print('The dicount must be between 0 and 100')
    print('Program terminated due to multiple incorrect inputs')
    return -1

def main():
    item1 = input_itemprice(1)
    if item1 == -1:
        return
    item2 = input_itemprice(2)
    if item2 == -1:
        return
    item3 = input_itemprice(3)
    if item3 == -1:
        return
    print()
    disc1 = input_discount(1)
    if disc1 == -1:
        return
    disc2 = input_discount(2)
    if disc2 == -1:
        return
    disc3 = input_discount(3)
    if disc3 == -1:
        return
    disc4 = 0.72
    print()
    phnum = input_phnum()
    if phnum == -1:
        return
    print()
    print('The resulting catalog is:-')
    print()
    print('-'*60)
    print('Delhi Days\nR-Block, Model Town 3\nDelhi: 110009')
    print()
    print('Item             Price')
    print('-'*25)
    print('Item 1           %.2f' %item1)
    print('Item 2           %.2f' %item2)
    print('Item 3           %.2f' %item3)
    print('Combo Pack 1     %.2f' %((item1 + item2)*disc1))
    print('Combo Pack 2     %.2f' %((item1 + item3)*disc2))
    print('Combo Pack 3     %.2f' %((item2 + item3)*disc3))
    print('Super Saver      %.2f' %((item1 + item2 + item3)*disc4))
    print()
    print('For home delivery, contact here:', phnum)

#Driver Code
print('-'*60)
main()
print('-'*60)