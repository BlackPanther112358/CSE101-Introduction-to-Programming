import math

#Declaring functions
def custom_inpt_float(string:str)->float: #Function for taking float input
    cnt = 0
    while(cnt < 3):
        cnt += 1
        try:
            inpt = float(input(string).strip())
            return inpt
        except:
            print('Please enter valid input')
            continue
    return -1

def custom_inpt_int(string:str)->int: #Function for taking integer input
    cnt = 0
    while(cnt < 3):
        cnt += 1
        try:
            inpt = int(input(string).strip())
            return inpt
        except:
            print('Please enter valid input')
            continue
    return -1

def square()->bool:
    side = custom_inpt_float('Please enter the length of the side: ')
    if(side == -1):
        return False
    print('The perimeter of the square is %.2f' %(side*4))
    print('The area of the square is %.2f' %(side*side))
    return True

def rectangle()->bool:
    length = custom_inpt_float('Please enter the length of the rectangle: ')
    if(length == -1):
        return False
    breadth = custom_inpt_float('Please enter the breadth of the rectangle: ')
    if(breadth == -1):
        return False
    print('The perimeter of the rectangle is %.2f' %(2*(length + breadth)))
    print('The area of the rectangle is %.2f' %(length*breadth))
    return True

def rhombus()->bool:
    side = custom_inpt_float('Please enter the side of the rhombus: ')
    if(side == -1):
        return False
    diagonal1 = custom_inpt_float('Please enter first diagonal of the rhombus: ')
    if(diagonal1 == -1):
        return False
    diagonal2 = custom_inpt_float('Please enter second diagonal of the rhombus: ')
    if(diagonal2 == -1):
        return False
    print('The perimeter of the rhombus is %.2f' %(side*4))
    print('The area of the rhombus is: %.2f' %(diagonal1*diagonal2))
    return True

def parallelogram()->bool:
    length = custom_inpt_float('Please enter the length of the parallelogram: ')
    if(length == -1):
        return False
    breadth = custom_inpt_float('Please enter the breadth of the parallelogram: ')
    if(breadth == -1):
        return False
    heigth = custom_inpt_float('Please enter the height of the parallelogram: ')
    if(heigth == -1):
        return False
    print('The perimeter of the parallelogram is %.2f' %(2*(length + breadth)))
    print('The area of the parallelogram is: %.2f' %(length*heigth))
    return True

def circle()->bool:
    radius = custom_inpt_float('Please enter the radius of the circle: ')
    if(radius == -1):
        return False
    print('The perimeter of the circle is %.2f' %(2*math.pi*radius))
    print('The area of the circle is %.2f' %(math.pi*radius*radius))
    return True

def cube()->bool:
    side = custom_inpt_float('Please enter the length of the cube: ')
    if(side == -1):
        return False
    print('The Curved surface area of the cube is %.2f' %(4*side*side))
    print('The Total surface area of the cube is %.2f' %(6*side*side))
    print('The Volume of the cube is %.2f' %(side*side*side))
    return True

def cuboid()->bool:
    length = custom_inpt_float('Please enter the length of the cuboid: ')
    if(length == -1):
        return False
    breadth = custom_inpt_float('Please enter the breadth of the cuboid: ')
    if(breadth == -1):
        return False
    heigth = custom_inpt_float('Please enter the height of the cuboid: ')
    if(heigth == -1):
        return False
    print('The Curved surface area of the cuboid is %.2f' %(2*heigth*(length + breadth)))
    print('The Total surface area of the cuboid is %.2f' %(2*(length*breadth + length*heigth + heigth*breadth)))
    print('The Volume of the cuboid is %.2f' %(length*breadth*heigth))
    return True

def right_circular_cone()->bool:
    slant_height = custom_inpt_float('Please enter the slant height of the cone: ')
    if(slant_height == -1):
        return False
    height = custom_inpt_float('Please enter the height of the cone: ')
    if(height == -1):
        return False
    radius = custom_inpt_float('Please enter the radius of the cone: ')
    if(radius == -1):
        return False
    print('The Curved surface area of the cone is %.2f' %(math.pi*radius*slant_height))
    print('The Total surface area of the cone is %.2f' %(math.pi*radius*slant_height + math.pi*radius*radius))
    print('The Volume of the cone is %.2f' %(0.5*math.pi*radius*radius*height))
    return True

def hemisphere()->bool:
    radius = custom_inpt_float('Please enter the radius of the hemisphere: ')
    if(radius == -1):
        return False
    print('The Curved surface area of the hemisphere is %.2f' %(2*math.pi*radius*radius))
    print('The Total surface area of the hemisphere is %.2f' %(3*math.pi*radius*radius))
    print('The Volume of the hemisphere is %.2f' %((2/3)*math.pi*radius*radius*radius))
    return True
    
def sphere()->bool:
    radius = custom_inpt_float('Please enter the radius of the sphere: ')
    if(radius == -1):
        return False
    print('The Curved surface area of the sphere is %.2f' %(4*math.pi*radius*radius))
    print('The Total surface area of the sphere is %.2f' %(4*math.pi*radius*radius))
    print('The Volume of the sphere is %.2f' %((4/3)*math.pi*radius*radius*radius))
    return True

def solid_cylinder()->bool:
    height = custom_inpt_float('Please enter the height of the solid cylinder: ')
    if(height == -1):
        return False
    radius = custom_inpt_float('Please enter the radius of the solid cylinder: ')
    if(radius == -1):
        return False
    print('The Curved surface area of the solid cylinder is %.2f' %(2*math.pi*radius*height))
    print('The Total surface area of the solid cylinder is %.2f' %(2*math.pi*radius*height + 2*math.pi*radius*radius))
    print('The Volume of the solid cylinder is %.2f' %(math.pi*radius*radius*height))
    return True

def hollow_cylinder()->bool:
    height = custom_inpt_float('Please enter the height of the solid cylinder: ')
    if(height == -1):
        return False
    radius1 = custom_inpt_float('Please enter the radius of the solid cylinder: ')
    if(radius1 == -1):
        return False
    radius2 = custom_inpt_float('Please enter the radius of the solid cylinder: ')
    if(radius2 == -1):
        return False
    print('The Curved surface area of the solid cylinder is %.2f' %(2*math.pi*(radius1 + radius2)*height))
    print('The Total surface area of the solid cylinder is %.2f' %(2*math.pi*(radius1 + radius2)*height + 2*math.pi*(radius1*radius1 - radius2*radius2)))
    print('The Volume of the solid cylinder is %.2f' %(math.pi*(radius1*radius1 - radius2*radius2)*height))
    return True

#Driver Code
#Lists for possible inputs
shapes = ['Square', 'Rectangle', 'Rhombus', 'Parallelogram', 'Circle', 'Cube', 'Cuboid', 'Right Circular Cone', 'Hemisphere', 'Sphere', 'Solid Cylinder', 'Hollow Cylinder']
dimensions = ['2d', '3d']

print('-'*60)
students = custom_inpt_int('Please enter the number of students: ')     #input for no. of students
while(students == -1):
    students = custom_inpt_int('Please enter the number of students: ')
for _ in range(students):
    dim = -1
    while(dim == -1):
        try:
            dim = dimensions.index(input('Please choose whether shape is 2D or 3D: ').strip().lower())      #Input for 2D/3D
        except ValueError:
            print('Please enter a valid input')
            continue
    print()
    if dim == 0:
        print('Please choose one of the following options by entering the its serial no.:-')
        for num, shape in enumerate(shapes[:5]):    #Loop for printing the options
            print('%i) %s' %((num + 1), shape))
        idx = custom_inpt_int('Serial no. of required shape: ')
        if(idx == -1):
            print('Program terminated due to multiple invalid inputs')
            break
        elif(idx == 1):
            if(not(square())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 2):
            if(not(rectangle())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 3):
            if(not(rhombus())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 4):
            if(not(parallelogram())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 5):
            if(not(circle())):
                print('Program terminated due to multiple invalid inputs')
                break
        else:
            print('Invalid serial number, Program terminated')
            break
    else:
        print('Please choose one of the following options by entering the its serial no.:-')
        for num, shape in enumerate(shapes[5::]):       #Loop for printing the options
            print('%i) %s' %((num + 1), shape))
        idx = custom_inpt_int('Serial no. of required shape: ')
        if(idx == -1):
            print('Program terminated due to multiple invalid inputs')
            break
        elif(idx == 1):
            if(not(cube())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 2):
            if(not(cuboid())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 3):
            if(not(right_circular_cone())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 4):
            if(not(hemisphere())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 5):
            if(not(sphere())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 6):
            if(not(solid_cylinder())):
                print('Program terminated due to multiple invalid inputs')
                break
        elif(idx == 7):
            if(not(hollow_cylinder())):
                print('Program terminated due to multiple invalid inputs')
                break
        else:
            print('Invalid serial number, Program terminated')
            break
    print()
print('-'*60)
