#Declaring global variables
id = 0

#Declaring class
class LaundryService:
    def __init__(self, name, phno, email, cloth, branded, season):
        global id
        id += 1
        self.id = id
        self.name = name
        self.phno = phno
        self.email = email
        self.cloth = cloth
        self.branded = branded
        self.season = season
        self.price = {'Cotton':50, 'Silk':30, 'Woolen':90, 'Polyester':20}
    def customerDetails(self):
        x = lambda a:'True' if a else 'False'
        print(f'Customer ID: {self.id}')
        print(f'Name of customer: {self.name}')
        print(f'Contact no.: {self.phno}')
        print(f'Email: {self.email}')
        print(f'Type of cloth: {self.cloth}')
        print(f'Branded or not: {x(self.branded)}')
    def calculateCharge(self):
        cost = self.price[self.cloth]
        if self.branded:
            cost *= 1.5
        if self.season == 'Winter':
            cost /= 2
        else:
            cost *= 2
        return cost
    def finalDetails(self):
        self.customerDetails()
        charge = self.calculateCharge()
        print(f'Total Charge: Rs.{charge:.2f}')
        if charge > 200:
            print('To be returned in 4 days')
        else:
            print('To be returned in 7 days')

#Declaring Functions
def input_num(text):
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = int(input(text).strip())
            if inpt > 0:
                return inpt
            print('Please enter a positive value.')
        except ValueError:
            print('Please enter an integral value.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_yesorno():
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input('Please enter if it is branded: ').strip()
            if inpt.lower() in ['y', 'yes', '1']:
                return 1
            elif inpt.lower() in ['n', 'no', '0']:
                return 0
            else:
                print('Please enter \'Yes\' or \'No\'')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_phno()->int:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input('Please enter your phone number: ')
            if len(inpt) != 10:
                print('The phone number should have 10 digits')
                continue
            if(inpt[0] == '0'):
                print('The first number cannot be 0')
                continue
            if(inpt.isdigit()):
                return int(inpt)
            else:
                print('Please enter digits from 0 to 9')
        except Exception:
            print('Please enter input in correct format')
            continue
    return False

def input_string(possibilities:list, text:str)->str:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input(text).strip()
            if inpt.capitalize() in possibilities:
                return inpt.capitalize()
            print('Please enter a valid input')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_name()->str:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input('Please enter the name: ').strip()
            check = True
            for i in inpt:
                if (ord(i) not in range(65, 91)) and (ord(i) not in range(97, 123) and (i != ' ')):
                    check = False
                    break
            if not(check):
                print('The name can only contain alphabets and spaces.')
                continue
            return inpt
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_email()->str:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input('Please enter your email id: ')
            if (inpt.count('@') == 1) and (inpt.count('.') == 1):
                return inpt
            print('Please enter a valid email id')
        except Exception:
            print('Please enter input in correct format')
            continue
    return False

def process_cust():
    name = input_name()
    if name is False:
        return False
    ph = input_phno()
    if ph is False:
        return False
    email = input_email()
    if email is False:
        return False
    cloth = input_string(['Cotton', 'Silk', 'Woolen', 'Polyester'], 'Please enter the type of cloth: ')
    if cloth is False:
        return False
    branded = input_yesorno()
    if branded is False:
        return False
    season = input_string(['Winter', 'Summer'], 'Please enter the season: ')
    if season is False:
        return False
    cust = LaundryService(name, ph, email, cloth, branded, season)
    print('\n')
    cust.finalDetails()
    return True

def main():
    cust_cnt = input_num('Please enter the number of customers: ')
    print()
    if cust_cnt is False:
        return
    for _ in range(cust_cnt):
        if process_cust() is False:
            return
        print()
    return

if __name__ == '__main__':
    print('-' * 75)
    main()
    print('-' * 75)