#Initialising global variables
e = tuple() #Origin of ray
d = tuple() #Direction of ray
o = tuple() #Center of sphere
r = 0       #Radius of sphere

#Declaring functions
def input_radius()->float:  #Function for taking float input, used in input_vector()
    cnt = 0
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input('Please enter the radius of sphere: ').strip())
        except:
            print('Please enter a valid value for radius')
            continue
        if(inpt >= 0):
            return inpt
        print('Radius cannot be less than 0.')
    print('The program terminated due to multiple incorrect inputs')
    return -1

def input_float(string:str)->float: #Function for inputtind radius
    cnt = 0
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input(string).strip())
            return inpt
        except:
            print('Please enter a valid value for coordinates')
            continue
    print('The program terminated due to multiple incorrect inputs')
    return False

def input_vector(string:str)->tuple:    #Function for inputting a vector
    ans_tup = tuple()
    val = input_float('Please enter the x-coordinate of ' + string + ': ')
    if val is False:
        return False
    ans_tup += (val,)    
    val = input_float('Please enter the y-coordinate of ' + string + ': ')
    if val is False:
        return False
    ans_tup += (val,)
    val = input_float('Please enter the z-coordinate of ' + string + ': ')
    if val is False:
        return False
    ans_tup += (val,)
    return ans_tup

def point(t:float)->tuple:      #Function to return the coordinates for parameter t
    ans = tuple()
    for i in range(3):
        ans += (e[i] + t*d[i],)
    return ans

def closest_to_center()->float: #Function to return value of t, such that point is closest to the center of sphere
    den = sum([i*i for i in d])
    num = 0
    for i in range(3):
        num += d[i]*(o[i] - e[i])
    return  num/den

def distance_along_d(t:float)->float:  #Function to return value t - t_min (point of intersection)
    foot = point(t)
    dist = 0
    for i in range(3):
        dist += pow(o[i] - foot[i], 2)
    dist = pow(dist, 0.5)
    if(dist > r):
        return False
    if abs(dist - r) < 0.001:
        return 0
    dist_dev = pow(r*r - dist*dist, 0.5)
    mod = 0
    for i in d:
        mod += i*i
    mod = pow(mod, 0.5)
    return dist_dev/mod

def print_points(points:set):   #Function to print points of intersection
    print('There are %i points of intersection' %len(points))
    if(len(points) == 0):
        return
    print('Following are the points in (x, y, z) format:-')
    for t in points:
        print(point(t))
    return

def main():
    global e, d, o, r
    e = input_vector('Origin of light ray')
    if e is False:
        return
    d = input_vector('Direction of light ray')
    if d is False:
        return
    o = input_vector('Center of sphere')
    if o is False:
        return
    r = input_radius()
    if r == -1:
        return
    print()
    t_min = closest_to_center()
    dev = distance_along_d(t_min)
    if dev is False:
        print('There are no points of intersection')
        return
    ans = set()
    if (t_min + dev) >= 0:
        ans.add(t_min + dev)
    if (t_min - dev) >= 0:
        ans.add(t_min - dev)
    print_points(ans)
    return

#Driver Code
print('-'*60)
main()
print('-'*60)