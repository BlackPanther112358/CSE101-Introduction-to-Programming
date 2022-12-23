#Defining Functions
def input_int(msg:str)->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            num = int(input(msg).strip())
        except Exception:
            print('Pleas enter an integer value.')
            continue
        if num > 0:
            return num
        print('Please enter a positive integer.')
    print('Program terminated due to multiple invalid inputs.')
    return False

def input_line(length:int)->list:   #For taking input of each line of matrix
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            line = list(map(float, input('Please enter the space separated input for row of matrix: ').split()))
        except Exception:
            print('Please provide input as space separated integers')
            continue
        if len(line) == length:
            return line
        else:
            print(f'Please enter exactly {length} integers in a single line.')
    print('Program terminated due to multiple incorrect inputs.')
    return False

def input_matrix(dim:int)->list:             #For taking input of matrix
    matrix = []
    for _ in range(dim):
        line = input_line(dim)
        if line is False:
            return False
        matrix.append(line)
    return matrix   

def normal_traversal(dim:int, matrix:list):
    print('The normal traversal of the given matrix is as follows:-')
    for row in range(dim):
        for col in range(dim):
            print(matrix[row][col], end = ' ')
    print()
    return

def alternating_traversal(dim:int, matrix:int):
    print('The alternating traversal of the given matrix is as follows:-')
    for row in range(dim):
        if row%2:
            lst = [i for i in range(dim - 1, -1, -1)]
        else:
            lst = [i for i in range(dim)]
        for col in lst:
            print(matrix[row][col], end = ' ')
    return

def spiral_traversal(dim:int, matrix:int):
    print('The spiral traversal of the given matrix is as follows:-')
    for itr in range(dim//2):
        for col in range(itr, dim - itr):          
            print(matrix[itr][col], end = ' ')      
        for row in range(itr + 1, dim - itr - 1):  
            print(matrix[row][dim - itr - 1], end = ' ')  
        for col in range(dim - itr - 1, itr - 1, -1):      
            print(matrix[dim - itr - 1][col], end = ' ')  
        for row in range(dim - itr - 2, itr, -1):        
            print(matrix[row][itr], end = ' ')        
    if dim%2:
        print(matrix[dim//2][dim//2], end = ' ')
    print()
    return

def boundary_traversal(dim:int, matrix:int):
    print('The boundary traversal of the given matrix is as follows:-')
    if dim == 1:
        print(matrix[0][0])
        return
    for col in range(dim):
        print(matrix[0][col], end = ' ')
    for row in range(1, dim - 1):
        print(matrix[row][dim - 1], end = ' ')
    for col in range(dim - 1, -1, -1):
        print(matrix[dim - 1][col], end = ' ')
    for row in range(dim - 2, 0, -1):
        print(matrix[row][0], end = ' ')
    print()
    return

def diagnol_traversal_r(dim:int, matrix:int):
    print('The diagnol traversal of the given matrix from right to left is as follows:-')
    for diff in range(1 - dim, dim):
        for row in range(max(diff, 0), min(diff + dim, dim)):
            print(matrix[row][row - diff], end = ' ')
    print()
    return

def diagnol_traversal_l(dim:int, matrix:int):
    print('The diagnol traversal of the given matrix from left to right is as follows:-')
    for add in range(0, 2*dim - 1):
        for row in range(max(add - dim + 1, 0), min(add + 1, dim)):
            print(matrix[row][add - row], end = ' ')
    print()
    return

def main():
    menu = ['Normal traversal', 'Alternating traversal', 'Spiral traversal', 'Boundary traversal', 'Diagnol traversal from right to left', 
    'Diagnol traversal from left to right', 'Exit']
    n = input_int('Please enter the dimensions of square matrix: ')
    if n is False:
        return
    matrix = input_matrix(n)
    if matrix is False:
        return
    print('Please choose one of the following:-')
    for i, option in enumerate(menu):
        print(f'{i + 1}) {option}')
    choice = input_int('Please enter your choice: ')
    if choice > 7:  
        print('Invalid choice, only 7 options available')
        return
    if choice == 1:
        normal_traversal(n, matrix)
    elif choice == 2:
        alternating_traversal(n, matrix)
    elif choice == 3:
        spiral_traversal(n, matrix)
    elif choice == 4:
        boundary_traversal(n, matrix)
    elif choice == 5:
        diagnol_traversal_r(n, matrix) 
    elif choice == 6:
        diagnol_traversal_l(n, matrix)
    elif choice == 7:
        print('The program has been terminated.')
        return
    return

#Driver code
if __name__ == '__main__':
    print('-'*100)
    main()
    print('-'*100)