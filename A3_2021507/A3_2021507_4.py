#Declaring global variables
Persons = [] 

#Defining class Person
class Person:
    def __init__(self, firstname, lastname, age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def __repr__(self) -> str:
        return f'{self.firstname} {self.lastname} {self.age}'

#Creating functions
def input_yesno(text)->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input(text).strip()
            if inpt.lower() in ['no', 'n']:
                return 0
            elif inpt.lower() in ['yes', 'y']:
                return 1
            else:
                print('Please enter either Y or N.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_int(text:str)->int:
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
                if (ord(i) not in range(65, 91)) and (ord(i) not in range(97, 123)):
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

def input_person(cnt:int)->Person:
    firstname = input_name(f'Enter the firstname of Person {cnt}: ')
    if firstname is False:
        return False
    lastname = input_name(f'Enter the lastname of Person {cnt}: ')
    if lastname is False:
        return False
    age = input_int(f'Enter the age of Person {cnt}: ')
    if age is False:
        return False
    print()
    return Person(firstname, lastname, age)

def input_attr(cnt:int)->str:
    try_cnt = 0
    while try_cnt < 3:
        try:
            inpt = input(f'Query {cnt}: ').strip()
            if inpt.lower() in ['firstname', 'lastname', 'age']:
                return inpt.lower()
            else: 
                print('Please enter a valid attribute.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple invalid inputs')
    return False

def sort_attribute(attr:str)->None:
    sorted_Persons = sorted(Persons, key = lambda x:getattr(x, attr))
    print('Order:')
    for person in sorted_Persons:
        print(person)
    print()

def main()->None:
    global Persons
    print('Welcome to the application!\n')
    while True:
        person_num = input_int('Specify the number of people to be enrolled: ')
        print()
        if person_num is False:
            return
        for i in range(person_num):
            inpt_person = input_person(i + 1)
            if inpt_person is False:
                return
            Persons.append(inpt_person)
        query_num =  input_int('Specify the number of queries: ')
        print()
        if query_num is False:
            return
        for i in range(query_num):
            inpt_query = input_attr(i + 1)
            print()
            if inpt_query is False:
                return
            sort_attribute(inpt_query)
        print()
        bool_ans = input_yesno('Thanks for using the Application, if you wish to restart, press “Y” else press “N” to exit: ')
        if bool_ans is False:
            return
        elif bool_ans == 0:
            print('Program terminated')
            return
        Persons = []

if __name__ == '__main__':
    print('-' * 75)
    main()
    print('-' * 75)