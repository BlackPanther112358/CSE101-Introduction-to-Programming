#Importing required functions
from cases import generateData

#Defining functions
def input_int()->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            num = int(input('Please enter the number of test cases to run: ').strip())
        except Exception:
            print('Pleas enter an integer value.')
            continue
        if num > 0:
            return num
        print('Please enter a positive integer.')
    print('Program terminated due to multiple invalid inputs.')
    return False

def readCase(num:int)->tuple:
    input_file_name = r'A2_2021507_B1\Input_' + str(num) + '.txt'
    output_file_name = r'A2_2021507_B1\Output_' + str(num) + '.txt'
    with open(input_file_name,'r') as f_read:
        input_str = f_read.read()
    input_str.strip(r'\n')
    input_arr = list(map(int, input_str.split()))
    with open(output_file_name,'r') as f_read:
        output_str = f_read.read()
    output_str.strip(r'\n')
    output_arr = list(map(int, output_str.split()))
    return tuple([input_arr, output_arr])

def function2(arr:list)->list:    
    length = len(arr)
    for i in range(length - 2, -1, -1):
        for j in range(i + 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

def check(num:int)->bool:
    arr, ans_arr = readCase(num)
    sorted_arr = function2(arr)
    if sorted_arr == ans_arr:
        return True
    return False

def testing(n:int)->int:
    success = 0
    for num in range(1, n + 1):
        if check(num):
            success += 1
    return success

def main():
    n = input_int()
    print('NOTE: Sorting large number of cases may take time.')
    if n is False:
        return
    check = generateData(n)
    if check is False:
        return
    print()
    print(f'Data generated for {n} testcases. Running testcases.')
    print()
    success = testing(n)
    print('Testing completed')
    print(f'Successful cases: {success}/{n}')
    print()
    if success == n:
        print('SUCCESS')
    else:
        print('FAILED')
    return

#Driver code
if __name__ == '__main__':
    print('-' * 100)
    main()
    print('-' * 100)