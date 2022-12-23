#declaring global values
stv = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30,
 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
vts = dict(map(reversed, stv.items()))

#Declaring fuctions
def input_option(limit:int)->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = int(input('Please choose an option: ').strip())
            if inpt in range(1, limit + 1):
                return inpt
            else:
                print(f'Please enter an integer between 1 and {limit}')
                continue
        except Exception:
            print('Please enter an integer')
            continue
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_base(msg:str)->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = int(input(msg).strip())
            if inpt in range(1, 37):
                return inpt
            else:
                print(f'Please enter an integer between 1 and 36')
                continue
        except Exception:
            print('Please enter an integer')
            continue
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_num(base:int)->str:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input('Please enter the number to convert: ').strip()
            check = True
            idx = 0
            if inpt[0] == '-':
                idx = 1
            for char in inpt[idx::]:
                if char not in stv.keys():
                    print('Invalid character entered. Characters of input should be either uppercase letters or digits, and have no radix point')
                    check = False
                    break
                elif stv[char] >= base:
                    print('Incorrect characters entered for the corresponding base')
                    check = False
                    break
            if check:
                return inpt
        except Exception:
            print('Please enter a valid input')
            continue
    print('Program terminated due to multiple incorrect inputs')
    return False

def basexto10(base:int, num:str)->int:
    is_neg = False
    if num[0] == '-':
        is_neg = True
        num = num[1::]
    num_10 = 0
    for char in num:
        num_10 *= base  
        num_10 += stv[char]
    if is_neg:
        num_10 = -num_10
    return num_10

def base10tox(base:int, num:int)->str:
    if num == 0:
        return '0'
    is_neg = False
    if num < 0:
        is_neg = True
        num = abs(num)
    num_x = ''
    while num:
        num, rem = num//base, num%base
        num_x += vts[rem]
    return '-'*is_neg + num_x[::-1]

def convert(init_base:int, final_base:int, num:str)->str:
    print(f'{num} when converted from base {init_base} to base {final_base} is {base10tox(final_base, basexto10(init_base, num))}')
    return

def main():
    print('NOTE: The following program converts any number from one base to another, as long as both bases are atmost 36.\n')
    print('Choose one of the following options:-')
    menu = ['Convert decimal to binary and vice-versa', 'Convert decimal to hexadecimal and vice-versa', 'Convert decimal to octal and vice-versa.',
    'Convert binary to hexadecimal and vice-versa.', 'Convert binary to octal and vice-versa.', 'Convert hexadecimal to octal and vice-versa.',
    'Convert number with radix A to radix B.']
    for no, option in enumerate(menu):
        print(f'{no + 1}) {option}')
    print()
    option = input_option(7)
    if option is False:
        return
    print()
    if option == 1:
        bases = [['Binary', 2], ['Decimal', 10]]
        print(f'1) Convert from {bases[0][0]} to {bases[1][0]}')
        print(f'2) Convert from {bases[1][0]} to {bases[0][0]}')
        option = input_option(2)
        if option is False:
            return
        print()
        if option == 1:
            convert_num = input_num(bases[0][1])
            if convert_num is False:
                return
            print()
            convert(bases[0][1], bases[1][1], convert_num)
        else:
            convert_num = input_num(bases[1][1])
            if convert_num is False:
                return
            print()
            convert(bases[1][1], bases[0][1], convert_num)
    elif option == 2:
        bases = [['Hexadecimal', 16], ['Decimal', 10]]
        print(f'1) Convert from {bases[0][0]} to {bases[1][0]}')
        print(f'2) Convert from {bases[1][0]} to {bases[0][0]}')
        option = input_option(2)
        if option is False:
            return
        print()
        if option == 1:
            convert_num = input_num(bases[0][1])
            if convert_num is False:
                return
            print()
            convert(bases[0][1], bases[1][1], convert_num)
        else:
            convert_num = input_num(bases[1][1])
            if convert_num is False:
                return
            print()
            convert(bases[1][1], bases[0][1], convert_num)
    elif option == 3:
        bases = [['Octal', 8], ['Decimal', 10]]
        print(f'1) Convert from {bases[0][0]} to {bases[1][0]}')
        print(f'2) Convert from {bases[1][0]} to {bases[0][0]}')
        option = input_option(2)
        if option is False:
            return
        print()
        if option == 1:
            convert_num = input_num(bases[0][1])
            if convert_num is False:
                return
            print()
            convert(bases[0][1], bases[1][1], convert_num)
        else:
            convert_num = input_num(bases[1][1])
            if convert_num is False:
                return
            print()
            convert(bases[1][1], bases[0][1], convert_num)
    elif option == 4:
        bases = [['Binary', 2], ['Hexadecimal', 16]]
        print(f'1) Convert from {bases[0][0]} to {bases[1][0]}')
        print(f'2) Convert from {bases[1][0]} to {bases[0][0]}')
        option = input_option(2)
        if option is False:
            return
        print()
        if option == 1:
            convert_num = input_num(bases[0][1])
            if convert_num is False:
                return
            print()
            convert(bases[0][1], bases[1][1], convert_num)
        else:
            convert_num = input_num(bases[1][1])
            if convert_num is False:
                return
            print()
            convert(bases[1][1], bases[0][1], convert_num)
    elif option == 5:
        bases = [['Binary', 2], ['Octal', 8]]
        print(f'1) Convert from {bases[0][0]} to {bases[1][0]}')
        print(f'2) Convert from {bases[1][0]} to {bases[0][0]}')
        option = input_option(2)
        if option is False:
            return
        print()
        if option == 1:
            convert_num = input_num(bases[0][1])
            if convert_num is False:
                return
            print()
            convert(bases[0][1], bases[1][1], convert_num)
        else:
            convert_num = input_num(bases[1][1])
            if convert_num is False:
                return
            print()
            convert(bases[1][1], bases[0][1], convert_num)
    elif option == 6:
        bases = [['Hexadecimal', 16], ['Octal', 8]]
        print(f'1) Convert from {bases[0][0]} to {bases[1][0]}')
        print(f'2) Convert from {bases[1][0]} to {bases[0][0]}')
        option = input_option(2)
        if option is False:
            return
        print()
        if option == 1:
            convert_num = input_num(bases[0][1])
            if convert_num is False:
                return
            print()
            convert(bases[0][1], bases[1][1], convert_num)
        else:
            convert_num = input_num(bases[1][1])
            if convert_num is False:
                return
            print()
            convert(bases[1][1], bases[0][1], convert_num)
    else:
        init_base = input_base('Please enter the base to convert from: ')
        if init_base is False:
            return
        final_base = input_base('Please enter the base to convert to: ')
        if final_base is False:
            return
        convert_num = input_num(init_base)
        if convert_num is False:
            return
        convert(init_base, final_base, convert_num)
    
#Driver code
if __name__ == '__main__':
    print('-' * 100)
    main()
    print('-' * 100)