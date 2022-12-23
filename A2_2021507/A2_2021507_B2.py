#Defining functions
def input_2(mode:bool)->tuple:               #For taking input of 2 space separated integers
    if mode:
        ques = 'Please enter the dimensions of the city: '
    else:
        ques = 'Please enter the grammys won by Doja Dog and DJ Snack respectively: '
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            a, b = map(int, input(ques).split())
        except ValueError:
            print('Please enter only 2 integers as in input.')
            continue
        except Exception:
            print('Please provide input in proper format')
            continue
        if mode:
            if (a > 0) and (b > 0):
                return tuple([a, b])
            else:
                print('The dimensions of the city must be positive.')
        else:
            if (a >= 0) and (b >= 0):
                return tuple([a, b])
            else:
                print('The number of grammys must be non-negative.')
    print('Program terminated due to multiple incorrect inputs.')
    return False

def input_line(length:int)->list:   #For taking input of each line of skyscraper
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            line = list(map(int, input('Please enter the space separated string for skyline: ').split()))
        except Exception:
            print('Please provide input in proper format')
            continue
        if len(line) == length:
            nums = [0, 1]
            check = True
            for num in line:
                if num not in nums:
                    check = False
                    break
            if check:
                return line
            else:
                print('The input can contain only 0\'s and 1\'s')
        else:
            print(f'Please enter exactly {length} integers in a single line.')
    print('Program terminated due to multiple incorrect inputs.')
    return False

def input_city(height:int, width:int)->list:             #For taking input of city skyline
    skyline = []
    for _ in range(height):
        line = input_line(width)
        if line is False:
            return False
        skyline.append(line)
    return skyline

def sort_city(height:int, width:int, skyline:list)->list:   #For sorting the towers
    sorted_skyline = []
    for idx in range(width):
        skyscraper_height = 0
        flips, prev = 0, 0
        for i in range(height):
            skyscraper_height += skyline[i][idx]
            flips, prev = flips + (prev^skyline[i][idx]), skyline[i][idx]
        if flips != 1:
            print(f'The skyscraper at index {idx} is invalid.')
            return False
        sorted_skyline.append([skyscraper_height, idx])
    sorted_skyline = sorted(sorted_skyline, reverse=True)
    return sorted_skyline

def calculate(d_grammy:int, s_grammy:int, height:int, width:int, skyline:list)->tuple:              
    #For calculating answer, tuple :- (Doja Dog Reputation, DJ Snack Reputation, skyline)    
    fin_skyline = [[0 for _ in range(width)] for _ in range(height)]
    d_rep, s_rep = 0, 0
    for itr in range(width):
        skyscraper_height, idx = skyline[itr]
        if itr%2:
            char = 'S'
            s_rep += skyscraper_height*(s_grammy + itr)
        else:
            char = 'D'
            d_rep += skyscraper_height*(d_grammy + itr)
        for i in range(height-skyscraper_height, height):
            fin_skyline[i][idx] = char
    return tuple([d_rep, s_rep, fin_skyline])   

def output(d_grammy:int, s_grammy:int, height:int, width:int, skyline:list):    #For printing the required output
    d_rep, s_rep, skyline = calculate(d_grammy, s_grammy, height, width, skyline)
    print(f'Doja Dog has {d_rep} reputation in the end')
    print(f'DJ Snack has {s_rep} reputation in the end')
    print('The following is the skyline of the city:-')
    for line in skyline:
        print(*line)
    return

def main():
    inpt = input_2(False)
    if inpt is False:
        return
    p, q = inpt
    inpt = input_2(True)
    if inpt is False:
        return
    n, m = inpt
    city = input_city(n, m)
    if city is False:
        return
    city = sort_city(n, m, city)
    if city is False:
        return
    print()
    output(p, q, n, m, city)
    return

#Driver code
if __name__ == '__main__':
    print('-'*100)
    main()
    print('-'*100)