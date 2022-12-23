#Importing required functions
from random import randint

#Defining functions
def writeCase(num:int, input_arr:list, output_arr:list):
    input_str = ' '.join([str(num) for num in input_arr])
    output_str = ' '.join([str(num) for num in output_arr])
    input_file_name = r'A2_2021507_B1\Input_' + str(num) + '.txt'
    output_file_name = r'A2_2021507_B1\Output_' + str(num) + '.txt'
    try:
        with open(input_file_name, 'w') as f_write:
            f_write.write(input_str)
        with open(output_file_name, 'w') as f_write:
            f_write.write(output_str)
    except Exception:
        print('Could bot write the required files. Please check the directory.')
        return False
    return True

def generateRandom()->list:
    arr = []
    for _ in range(randint(1, 1000)):
        arr.append(randint(1, 100000))
    return arr

def function1(arr:list)->list:    
    if len(arr) == 1:
        return arr
    mid = (len(arr) + 1)//2
    arr1 = function1(arr[:mid])
    arr2 = function1(arr[mid::])
    i, j = 0, 0
    new_arr = []
    for _ in range(len(arr)):
        if i == len(arr1):
            num = arr2[j]
            j += 1
        elif j == len(arr2):
            num = arr1[i]
            i += 1
        else:
            if arr1[i] > arr2[j]:
                num = arr2[j]
                j += 1
            else:
                num = arr1[i]
                i += 1
        new_arr.append(num)
    return new_arr

def generateData(n:int):
    for num in range(1, n + 1):
        arr = generateRandom()
        sorted_arr = function1(arr)
        check = writeCase(num, arr, sorted_arr)
        if check is False:
            return False
    return

#Driver code
if __name__ == '__main__':
    raise Exception('Please driectly run the file test.py.')