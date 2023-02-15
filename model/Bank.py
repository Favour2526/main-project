import random

class Bank_login:
     
    def __init__(self,surname,firstname,age,tel_number,pin,account_number,account_balance):
        self.surname = surname
        self .firstname = firstname
        self.age = age
        self.tel_number = tel_number
        self.pin = pin
        self.account_number = account_number
        self.account_balance = account_balance

    def generate_user_surname(self):
        surname = input('Enter your surname\n')
        while len(surname) <= 1:
            print('Input error')
            surname = input('Enter your surname\n')
        return surname 

    def generate_user_firstname(self):
        firstname = input('Enter your firstname\n')
        while len(firstname) <= 1:
            print('Input error')
            firstname = input('Enter your firstname\n')
        return firstname 

    def generate_user_age(self):
        age = int(input('Enter your age\n'))
        while age < 18:
            print('You must be 18 or 18+ to open this account')
            age = int(input('Enter your age\n'))
        return age

    def generate_user_mobile_number(self):
        tel_number = input('Enter your mobile number\n')
        while len(tel_number) != 11:
            print('Input error')
            tel_number = input('Enter your mobile number\n')
        return tel_number

    def generate_user_pin(self):
        pin = input('Enter a four digit number\n')
        while len(pin) != 4:
            print('Input error')
            pin = input('Enter a four digit number\n')
        return pin

    def generate_account_number(self):
        accountnumber = random.randrange(1111111111,9999999999)
        self.account_number = accountnumber
        return random.randrange(1111111111,9999999999)

    def generate_account_balance(self):
        account_balance = (0.00)
        return account_balance

instance = Bank_login('surname', 'firstname', 'age', 'tel_number', 'pin', 'account_number', 'account_balance')
instance.generate_user_surname()
instance.generate_user_firstname()
instance.generate_user_age()
instance.generate_user_mobile_number()
instance.generate_user_pin()
instance.generate_account_number()
instance.generate_account_balance()
