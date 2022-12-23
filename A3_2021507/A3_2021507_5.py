#Declaring global variable
Students = []

#Defining classes
class Student:
    def __init__(self, name:str, cgpa:float, branch:str) -> None:
        self.name = name
        self.cgpa = cgpa
        self.branch = branch
        self.isPlaced = False

    def isEligible(self, company)->bool:  
        if self.isPlaced:
            return False
        if self.cgpa < company.requiredcgpa:
            return False
        if self.branch not in company.branches:
            return False
        return True

    def apply(self, company)->None:
        company.appliedStudents.append(self)

    def getsPlaced(self)->None:
        self.isPlaced = True

class Company:
    def __init__(self, name, cgpa, branches, positions) -> None:
        self.name = name
        self.requiredcgpa = cgpa
        self.branches = branches
        self.positionsOpen = positions
        self.appliedStudents = []
        self.applicationOpen = True

    def hireStudents(self)->None:  
        k = min(len(self.appliedStudents), self.positionsOpen)
        print(f'The company {self.name} has hired the following students:-')
        for student in self.appliedStudents[:k]:
            student.getsPlaced()
            print(student.name)
        print(f'The company has hired {k} students and {self.positionsOpen - k} positions are still vacant.')
        self.closeApplication()

    def closeApplication(self)->None:
        self.applicationOpen = False
        print()

#Declaring functions
def input_num(text:str)->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = int(input(text).strip())
            if inpt <= 0:
                print('The input must be positive.')
                continue
            return inpt
        except ValueError:
            print('Please enter an integral value.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_name(text:str)->str:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input(text).strip()
            check = True
            for i in inpt:
                if (ord(i) not in range(65, 91)) and (ord(i) not in range(97, 123)) and (i != ' '):
                    check = False
                    break
            if not(check):
                print('The name can only contain uppercase and lowercaase alphabets.')
                continue
            return inpt
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_cgpa(text:str)->float:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = float(input(text).strip())
            assert((inpt >= 0) and (inpt <= 10))
            return inpt
        except AssertionError:
            print('Please enter CGPA between 0 and 10')
        except ValueError:
            print('Please enter an integral value.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_branch(text:str)->str:        #Remove debugger
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input(text).strip()
            if inpt.upper() in ['CSAM', 'CSE', 'ECE']:
                return inpt.upper()
            print('Please enter a valid branch.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_branches()->list:
    branch_num = input_num('Enter the number of branches allowed by company: ')
    if branch_num is False:
        return False
    branches = []
    for i in range(branch_num):
        branch = input_branch(f'Enter branch {i + 1}: ')
        if branch is False:
            return False
        branches.append(branch)
    return branches

def input_student(cnt:int)->Student:
    name = input_name(f'Please enter the name of student {cnt}: ')
    if name is False:
        return False
    cgpa = input_cgpa(f'Please enter the cgpa of student {cnt}: ')
    if cgpa is False:
        return False
    branch = input_branch(f'Please enter the branch  of student {cnt}: ')
    if branch is False:
        return False
    return Student(name, cgpa, branch)

def input_company(cnt:int)->Company:
    name = input_name(f'Please enter the name of company {cnt}: ')
    if name is False:
        return False
    cgpa = input_cgpa(f'Please enter the required cgpa of company {cnt}: ')
    if cgpa is False:
        return False
    branches = input_branches()
    if branches is False:
        return False
    positions = input_num(f'Please enter the number of positions open in company {cnt}: ')
    if positions is False:
        return False
    return Company(name, cgpa, branches, positions)
    

def process_company(company:Company)->None:
    for student in Students:
        if student.isEligible(company):
            student.apply(company)
            print(f'Student {student.name} is eligible for Company {company.name}')
        else:
            print(f'Student {student.name} is not eligible for Company {company.name}')
    company.hireStudents()

def main():
    global Students
    student_num = input_num('Enter the number of students: ')
    if student_num is False:
        return
    print()
    for i in range(student_num):
        student = input_student(i + 1)
        if student is False:
            return
        Students.append(student)
        print()
    Students.sort(key=lambda x:x.cgpa, reverse=True)
    company_num = input_num('Enter the number of Companies: ')
    if company_num is False:
        return
    for i in range(company_num):
        company = input_company(i + 1)
        process_company(company)
        print()

if __name__ == '__main__':
    print('-' * 75)
    main()
    print('-' * 75)