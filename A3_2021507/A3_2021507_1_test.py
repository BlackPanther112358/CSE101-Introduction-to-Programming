#Importing the required file
import A3_2021507_1 as Transformations
import math
import random

#Making testcases
mult_tests = [[Transformations.Matrix([[1, 0, 2], [0, 2, 1], [2, 1, 0]]), Transformations.Matrix([[1], [2], [3]]), Transformations.Matrix([[7], [7], [4]])],
             [Transformations.Matrix([[1]]), Transformations.Matrix([[1]]), Transformations.Matrix([[1]])], 
             [Transformations.Matrix([[1, 0], [0, 1]]), Transformations.Matrix([[2], [2]]), Transformations.Matrix([[2], [2]])]]
scaling_tests = [[Transformations.Matrix([[1, 0, 2], [0, 2, 1], [2, 1, 0], [1, 1, 1]]), 0, 1, 0, Transformations.Matrix([[0, 0, 0], [0, 2, 1], [0, 0, 0], [1, 1, 1]])],
             [Transformations.Matrix([[1], [1], [1], [1]]), 1, 2, 3, Transformations.Matrix([[1], [2], [3], [1]])], 
             [Transformations.Matrix([[1, 0], [0, 1], [0, 0], [1, 1]]), 0, 0, 0, Transformations.Matrix([[0, 0], [0, 0], [0, 0], [1, 1]])]]
translation_tests = [[Transformations.Matrix([[1, 0, 2], [0, 2, 1], [2, 1, 0], [1, 1, 1]]), 1, 1, 1, Transformations.Matrix([[2, 1, 3], [1, 3, 2], [3, 2, 1], [1, 1, 1]])],
             [Transformations.Matrix([[1], [1], [1], [1]]), 0, 0, 0, Transformations.Matrix([[1], [1], [1], [1]])], 
             [Transformations.Matrix([[1, 0], [0, 1], [0, 0], [1, 1]]), 0, 2, 0, Transformations.Matrix([[1, 0], [2, 3], [0, 0], [1, 1]])]]
rotation_tests = [[Transformations.Matrix([[1, 0, 2], [0, 2, 1], [2, 1, 0], [1, 1, 1]]), 0, 0, Transformations.Matrix([[1, 0, 2], [0, 2, 1], [2, 1, 0], [1, 1, 1]])],
             [Transformations.Matrix([[1], [1], [1], [1]]), 1, math.pi, Transformations.Matrix([[-1], [1], [-1], [1]])], 
             [Transformations.Matrix([[1, 0], [0, 1], [0, 0], [1, 1]]), 2, math.pi/2, Transformations.Matrix([[0, -1], [1, 0], [0, 0], [1, 1]])]]

#Defining functions
def input_choice()->int:    #Function to input the choice from user
    try_count = 0
    while try_count < 3:
        try_count += 1
        try:
            num = int(input('Please enter your choice: ').strip())
            if ((num < 1) or (num > 4)):
                print('The input is should be between 1 and 4')
                continue
            return num
        except:
            print('Please enter a valid integer')
            continue
    print('Program Terminated due to multiple invalid inputs')
    return False

def matmul(mat_a:Transformations.Matrix, mat_b:Transformations.Matrix)->Transformations.Matrix:
    return mat_a*mat_b

def test_matmul(mat_a:Transformations.Matrix, mat_b:Transformations.Matrix, mat_fin:Transformations.Matrix)->bool:
    try:
        assert(matmul(mat_a, mat_b) == mat_fin)
    except AssertionError:
        return False
    return True

def test_scale(mat_a:Transformations.Matrix, sx:float, sy:float, sz:float, mat_fin:Transformations.Matrix)->bool:
    try:
        assert(Transformations.matrix_scale(sx, sy, sz, mat_a) == mat_fin)
    except AssertionError:
        return False
    return True

def test_translate(mat_a:Transformations.Matrix, tx:float, ty:float, tz:float, mat_fin:Transformations.Matrix)->bool:
    try:
        assert(Transformations.matrix_translate(tx, ty, tz, mat_a) == mat_fin)
    except AssertionError:
        return False
    return True

def test_rotate(mat_a:Transformations.Matrix, axis:int, phi:float, mat_fin:Transformations.Matrix)->bool:
    try:
        assert(Transformations.matrix_rotate(axis, phi, mat_a) == mat_fin)
    except AssertionError:
        return False
    return True

def test_query(mat:Transformations.Matrix, mat_fin:Transformations.Matrix, query:tuple)->int:
    query = query[2]
    if(query[0] == 'T'):
        return test_translate(mat, query[1], query[2], query[3], mat_fin)
    elif(query[0] == 'S'):
        return test_scale(mat, query[1], query[2], query[3], mat_fin)
    elif(query[0] == 'R'):
        return test_rotate(mat, query[1], query[2], mat_fin)
        
def main():
    test_num = Transformations.input_num('Please enter the number of test cases: ')
    if test_num is False:
        return
    mode = Transformations.input_yesno('Do you want to enter test cases manually?')
    if mode is False:
        return
    elif mode == 'yes':
        for _ in range(test_num):
            vertice_num = Transformations.input_num('Please enter the number of vertices: ')
            if vertice_num is False:
                return
            print('Please enter the initial matrix:-')
            coor_mat = Transformations.input_matrix(4, vertice_num)
            if coor_mat is False:
                return
            query = Transformations.input_query()
            if query[0] is False:
                return
            print('Please enter the final matrix:-')
            fin_mat = Transformations.input_matrix(4, vertice_num)
            if fin_mat is False:
                return
            print()
            if test_query(coor_mat, fin_mat, query):
                print('Test case Passed')
            else:
                print('Test case failed')
            print()
    else:
        menu = ['Test Multipication', 'Test Scaling', 'Test Translation', 'Test Rotation']
        print('Please choose one of the following: ')
        for sno, option in enumerate(menu):
            print(f'{sno + 1}) {option}')
        for _ in range(test_num):
            inpt = input_choice()
            if inpt is False:
                return
            elif inpt == 1:
                if test_matmul(*random.choice(mult_tests)):
                    print('Test case Passed')
                else:
                   print('Test case failed')
                print() 
            elif inpt == 2:
                if test_scale(*random.choice(scaling_tests)):
                    print('Test case Passed')
                else:
                   print('Test case failed')
                print()
            elif inpt == 3:
                if test_translate(*random.choice(translation_tests)):
                    print('Test case Passed')
                else:
                   print('Test case failed')
                print()
            elif inpt == 4:
                if test_rotate(*random.choice(rotation_tests)):
                    print('Test case Passed')
                else:
                   print('Test case failed')
                print()
    return

if __name__ == '__main__':
    print('-' * 75)
    main()
    print('-' * 75)