#Declaring Functions
def fun1(b1:bool)->bool:
    return((b1) and (not(b1)))

def fun2(b1:bool, b2:bool, b3:bool)->bool:
    return((b1 or b2) and (b2 or not(b3)))

def bool_char(var:bool)->str:
    if(var):
        return 'T'
    return 'F'

#Driver Code
bool_arr = [False, True]
print('-'*60)
print('The first boolean function is B1 \u00b7 ~B1')
print()
arr = [i for i in bool_arr if fun1(i)]
if(len(arr) == 0):
    print('The function is Unsatisfiable')
else:
    print('The function is satisfied by following values of B1:-')
    for i in arr:
        print(i, end = ' ')
    print()
print()
print('-'*60)
print('The second boolean function is (B1 + B2) \u00b7 (B2 + ~B3)')
print()
arr = [[i, j, k] for i in range(2) for j in range(2) for k in range(2) if fun2(i, j, k)]
if(len(arr) == 0):
    print('The function is Unsatisfiable')
else:
    print('The function is satisfied by following values:-')
    print('     B1      B2      B3')
    print('  ' + '-'*24)
    for i in arr:
        print('     %s       %s       %s' %(bool_char(i[0]), bool_char(i[1]), bool_char(i[2])))
print()
print('-'*60)