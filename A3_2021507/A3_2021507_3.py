#Importing the libraries
import getpass
from datetime import datetime as dt

#Declaring the required class
class BankAccount:
    def __init__(self, name, pswd, cur_bal):
        self.name = name
        self.pswd = pswd
        self.balance = cur_bal
        init_file(self.name + '.txt')
    def authenticate(self):
        trycnt = 0
        while True:
            try:
                trycnt += 1
                res = input_pass(1, self.pswd, 'Please enter your password: ')
                if  res == 1:
                    return True
                elif res is False:
                    return False
                assert(trycnt < 3)
            except AssertionError:
                print('Too many wrong attempts, Program terminated.')
                break
        return False
    def deposit(self):
        if self.authenticate() is False:
            return False
        amt = input_amount('Please enter the amount to be Depositted: ')
        if amt is False:
            return False
        self.balance += amt
        log(f'The amount of rupees {amt:.2f} has been added  Current balance -> {self.balance:.2f}', self.name + '.txt')
        return True
    def withdraw(self):
        if self.authenticate() is False:
            return False
        amt = input_amount('Please enter the amount to be Withdrawn: ')
        if amt is False:
            return False
        if amt > self.balance:
            print('Low balance!! Cannot be debited at this time!')
            return True
        self.balance -= amt
        log(f'The amount of rupees {amt:.2f} has been debited  Current balance -> {self.balance:.2f}', self.name + '.txt')
        return True
    def bankStatement(self):
        if self.authenticate() is False:
            return False
        file_name = self.name + '.txt'
        with open(file_name, 'r') as f_read:
            data = f_read.readlines()
            print(*data, sep = '')
        return True

#Defining the functions
def input_yesno(text):
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input(text).strip()
            if inpt.lower() in ['y', 'yes']:
                return 1
            elif inpt.lower() in ['n', 'no']:
                return 0
            else:
                print('Please enter \'Yes\' or \'No\'')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_option():
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = int(input('Please enter the appropriate option: ').strip())
            if inpt in range(1, 5):
                return inpt
            print('Please enter a number between 1 and 4')
        except ValueError:
            print('Please enter an integral value.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_str(text:str):
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input(text).strip()
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

def input_amount(text:str):
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = float(input(text).strip())
            if inpt > 0:
                return inpt
            print('Please enter a positive value.')
        except ValueError:
            print('Please enter a float value.')
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def input_pass(mode:int, password:str = '', text = str):
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = getpass.getpass(text).strip()
            if mode == 1:
                if inpt == password:
                    return 1
                else:
                    print('Incorrect Password')
            else:
                return inpt
        except Exception:
            print(f'Please enter input in valid format, {Exception} raised')
    print('Program terminated due to multiple incorrect inputs')
    return False

def init_file(name):
    with open(name, 'w') as f_write:
        f_write.write('')
    return

def log(text, name):
    with open(name, 'a') as f_append:
        f_append.write(str(dt.now()) + ' ' + text + '\n')
    return

def input_account()->BankAccount:
    name = input_str('Please enter your name: ')
    pswd = input_pass(mode=0, text='Please enter your password: ')
    bal = input_amount('Please enter the starting balance for your account: ')
    print()
    return BankAccount(name, pswd, bal)

def process_account(account:BankAccount):
    option_list = ['Deposit', 'Withdraw', 'Bank Statement', 'Exit']
    while True:
        print('Please choose one of the following options: ')
        for i,option in enumerate(option_list):
            print(f'{i + 1}) {option}')
        option_choosen = input_option()
        if option_choosen == 1:
            if account.deposit() is False:
                return
        elif option_choosen == 2:
            if account.withdraw() is False:
                return
        elif option_choosen == 3:
            account.bankStatement()
        else:
            return
        print()

def main():
    print('Welcome to the Bank of IIIT-D\n')
    acc = input_account()
    if acc is False:
        return
    process_account(acc)
    return

if __name__ == '__main__':
    print('-' * 75)
    main()
    print('-' * 75)