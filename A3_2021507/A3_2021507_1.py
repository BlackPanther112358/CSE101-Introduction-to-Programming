#The following file has been copied from Assignment-2, with a few modifications as demanded in Assigment-3

#Importing libraries
from math import sin, cos, radians

#Initialising class matrix for multiplying and printing matrices
class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list
        self.row = len(matrix_list)
        self.column = len(matrix_list[0])
    def __mul__(self, other):
        assert self.column == other.row, 'Invalid input for matrix multiplication'
        ans = [[] for _ in range(self.row)]
        for itr_row in range(self.row):
            for itr_col in range(other.column):
                val = 0
                for itr in range(self.column):
                    val += round(self.matrix[itr_row][itr]*other.matrix[itr][itr_col], 6)
                    val = round(val, 6)
                ans[itr_row].append(val)
        return(Matrix(ans))
    def __eq__(self, other):
        if (self.column != other.column) or (self.row != other.row):
            return False
        for i in range(self.row):
            for j in range(self.column):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True
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

#Declaring functions
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
                        ans = input_yesno(f'Is the angle {arg2} provided in radians ?')
                        if ans is False:
                            break
                        if ans == 'no':
                            arg2 = round(radians(arg2), 6)
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

def matrix_translate(tx:float, ty:float, tz:float, matrix:Matrix)->Matrix:
    coor_mat = Matrix([[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]])
    return coor_mat*matrix

def matrix_scale(sx:float, sy:float, sz:float, matrix:Matrix)->Matrix:
    coor_mat = Matrix([[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]])
    return coor_mat*matrix

def matrix_rotate(axis:int, phi:float, matrix:Matrix)->Matrix:
    if axis == 0:
        coor_mat = Matrix([[1, 0, 0, 0], [0, cos(phi), -sin(phi), 0], [0, sin(phi), cos(phi), 0], [0, 0, 0, 1]])
    elif axis == 1:
        coor_mat = Matrix([[cos(phi), 0, sin(phi), 0], [0, 1, 0, 0], [-sin(phi), 0, cos(phi), 0], [0, 0, 0, 1]])
    elif axis == 2:
        coor_mat = Matrix([[cos(phi), -sin(phi), 0, 0], [sin(phi), cos(phi), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    return coor_mat*matrix

def process_query(mat:Matrix, query:tuple)->Matrix:
    query = query[2]
    if(query[0] == 'T'):
        mat = matrix_translate(query[1], query[2], query[3], mat)
    elif(query[0] == 'S'):
        mat = matrix_scale(query[1], query[2], query[3], mat)
    elif(query[0] == 'R'):
        matrix = matrix_rotate(query[1], query[2], mat)
        if matrix is False:
            return False
    return mat

def main():
    num = input_num('Please enter the number of vertices: ')
    if num is False:
        return
    coor_mat = input_matrix(4, num)
    if coor_mat is False:
        return
    query_num = input_num('Please enter the number of queries: ')
    if query_num is False:
        return
    for _ in range(query_num):
        query = input_query()
        if query[0]:
            coor_mat = process_query(coor_mat, query)
            if coor_mat is False:
                return
        else:
            return
    print('The final vertices after the required transformations is:- ')
    coor_mat.output()
    return