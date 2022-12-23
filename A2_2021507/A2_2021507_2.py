#Importing libraries
from math import sin, cos, radians

#Declaring global variables
file_name = 'Q2_logs.txt'   #File used to save program logs

#Initialising class matrix for multiplying and printing matrices
class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list
        self.row = len(matrix_list)
        self.column = len(matrix_list[0])
    def __mul__(self, other):
        if self.column != other.row:
            return -1
        ans = [[] for _ in range(self.row)]
        for itr_row in range(self.row):
            for itr_col in range(other.column):
                val = 0
                for itr in range(self.column):
                    val += round(self.matrix[itr_row][itr]*other.matrix[itr][itr_col], 6)
                    val = round(val, 6)
                ans[itr_row].append(val)
        return(Matrix(ans))
    def output(self):
        print('x-coordinates: ', end = ' ')
        for x in self.matrix[0]:
            print(x, end = ' ')
        print()
        print('y-coordinates: ', end = ' ')
        for y in self.matrix[1]:
            print(y, end = ' ')
        print()
        print('z-coordinates: ', end = ' ')
        for z in self.matrix[2]:
            print(z, end = ' ')
        print()
        return
    def log(self):
        f_write = open(file_name, 'a')
        f_write.write('x-coordinates: ')
        for x in self.matrix[0]:
            f_write.write(str(x) + ' ')
        f_write.write('\n')
        f_write.write('y-coordinates: ')
        for y in self.matrix[1]:
            f_write.write(str(y) + ' ')
        f_write.write('\n')
        f_write.write('z-coordinates: ')
        for z in self.matrix[2]:
            f_write.write(str(z) + ' ')
        f_write.write('\n')
        f_write.close()
        return

#Declaring functions
def clear_files():
    with open(file_name, 'w') as f_write:
        f_write.write('')
    return

def input_yesno(msg:str):
    print(msg)
    try_cnt = 0
    while try_cnt < 3:
        inpt = input('Please enter Yes/No: ').strip()
        if inpt.lower() == 'yes':
            return 'yes'
        elif inpt.lower() == 'no':
            return 'no'
        else:
            print('Please enter a valid input')
        try_cnt += 1
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_num(msg:str)->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = int(input(msg).strip())
        except Exception:
            print('Please enter an integer')
            continue
        if inpt <= 0:
            print('Please enter a positive number')
            continue
        return inpt
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_query()->tuple:       #Output format:- (result, raw_input, processed_input), processed input is a tuple 
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            raw_inpt = input('Please enter the query in required format: ')
            inpt = raw_inpt.split()
            if (inpt[0] == 'T') and (len(inpt) == 4):
                try:
                    mode, arg1, arg2, arg3 = inpt
                    arg1, arg2, arg3 = round(float(arg1), 6), round(float(arg2), 6), round(float(arg3), 6)
                    return(tuple([True, raw_inpt, tuple([mode, arg1, arg2, arg3])]))
                except Exception:
                    print('Please enter a real number as the arguements')
                    continue
            elif (inpt[0] == 'S') and (len(inpt) == 4):
                try:
                    mode, arg1, arg2, arg3 = inpt
                    arg1, arg2, arg3 = round(float(arg1), 6), round(float(arg2), 6), round(float(arg3), 6)
                    return(tuple([True, raw_inpt, tuple([mode, arg1, arg2, arg3])]))
                except Exception:
                    print('Please enter a real number as the arguements')
                    continue
            elif (inpt[0] == 'R') and (len(inpt) == 3):
                try:
                    mode, arg1, arg2 = inpt
                    arg2 = round(float(arg2), 6)
                    try:
                        arg1 = ['x', 'y', 'z'].index(arg1.lower())
                        return(tuple([True, raw_inpt, tuple([mode, arg1, arg2])]))
                    except ValueError:
                        print('Please enter a valid axis input.')
                        continue
                except Exception:
                    print('Please enter a real number as the arguements')
                    continue
            else:
                print('Please enter the query in proper format')
                continue
        except Exception:
            print('Please enter a valid input.')
            continue
    print('Program terminated due to multiple invalid inputs')
    ans = tuple([False, raw_inpt, tuple()])
    return ans

def input_matrix_row(row:str, length:int)->list:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            arr = list(map(int, input(f'Please enter the values for coordinated of {row}: ').split()))
        except Exception:
            print('Please enter space seperated integers')
            continue
        if len(arr) == length:
            return arr
        print(f'The input should have {length} elements')
    print('Program terminated due to multiple invalid inputs')
    return False

def input_matrix(row:int, col:int)->Matrix:
    print()
    print('Please enter each row of the matrix as space seperated real numbers.')
    matrix = []
    lst = input_matrix_row('x', col)
    if lst is False:
        return False
    matrix.append(lst)
    lst = input_matrix_row('y', col)
    if lst is False:
        return False
    matrix.append(lst)
    lst = input_matrix_row('z', col)
    if lst is False:
        return False
    matrix.append(lst)
    lst = [1 for _ in range(col)]
    matrix.append(lst)
    return(Matrix(matrix))
    
def log_msg(msg:str):
    f_write = open(file_name, 'a')
    f_write.write(msg + '\n')
    f_write.close()

def log_query(query:tuple):
    f_write = open(file_name, 'a')
    if query[0]:
        f_write.write('\nThe input provided by user is:- \n')
        f_write.write(query[1])
        f_write.write('\n')
    else:
        f_write.write('The program terminated due to multiple invalid inputs\nLast input was:-\n')
        f_write.write(query[1])
        f_write.write('\n')
    f_write.close()
    return

def log_matrix(msg:str, matrix:Matrix):
    f_write = open(file_name, 'a')
    f_write.write(msg + '\n')
    f_write.close()
    matrix.log()
    return

def make_matrix_translate(tx:float, ty:float, tz:float)->Matrix:
    return Matrix([[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]])

def make_matrix_scale(sx:float, sy:float, sz:float)->Matrix:
    return Matrix([[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]])

def make_matrix_rotate(axis:int, phi:float)->Matrix:
    ans = input_yesno(f'Is the angle {phi} provided in radians ?')
    if ans is False:
        return False
    if ans == 'no':
        phi = round(radians(phi), 6)
    if axis == 0:
        return Matrix([[1, 0, 0, 0], [0, cos(phi), -sin(phi), 0], [0, sin(phi), cos(phi), 0], [0, 0, 0, 1]])
    elif axis == 1:
        return Matrix([[cos(phi), 0, sin(phi), 0], [0, 1, 0, 0], [-sin(phi), 0, cos(phi), 0], [0, 0, 0, 1]])
    elif axis == 2:
        return Matrix([[cos(phi), -sin(phi), 0, 0], [sin(phi), cos(phi), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

def process_query(coor_mat:Matrix, query:tuple)->Matrix:
    query = query[2]
    if(query[0] == 'T'):
        coor_mat = make_matrix_translate(query[1], query[2], query[3])*coor_mat
    elif(query[0] == 'S'):
        coor_mat = make_matrix_scale(query[1], query[2], query[3])*coor_mat
    elif(query[0] == 'R'):
        matrix = make_matrix_rotate(query[1], query[2])
        if matrix is False:
            log_msg('The program terminated due to incorrect input for whether the entered angle is in Radians or not.')
            return False
        coor_mat = matrix*coor_mat
    log_matrix('The matrix after processing the query is:', coor_mat)
    return coor_mat

def main():
    try:        #check if log file exists
        f_test = open(file_name, 'r')
        data = f_test.read()
        if data != '':
            ans = input_yesno('The previous logs are present in the file, do you want to overwrite it?')
            if ans is False:
                f_test.close()
                return
            if ans == 'no':
                f_test.close()
                print('Program terminated')
                return
        clear_files()
        print()
        f_test.close()
    except FileNotFoundError:
        pass
    num = input_num('Please enter the number of vertices: ')
    if num is False:
        log_msg('Program terminated due to incorrect input for number of vertices')
        return
    log_msg(f'The number of vertices in the matrix is {num}')
    coor_mat = input_matrix(4, num)
    if coor_mat is False:
        log_msg('Program terminated due to incorrect input for vertices')
        return
    log_matrix('The matrix provided as input are: ', coor_mat)
    query_num = input_num('Please enter the number of queries: ')
    if query_num is False:
        log_msg('Program terminated due to incorrect input for number of queries')
    for _ in range(query_num):
        query = input_query()
        log_query(query)
        if query[0]:
            coor_mat = process_query(coor_mat, query)
            if coor_mat is False:
                return
        else:
            return
    print('The final vertices after the required transformations is:- ')
    coor_mat.output()
    log_matrix('The final vertices after the required transformations is:- ', coor_mat)
    return

#Driver code
if __name__ == '__main__':
    print('-'*100)
    main()
    print('-'*100)