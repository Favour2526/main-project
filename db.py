import sqlite3
import time
from model.Bank import Bank_login

class Create_account(Bank_login):

    def __init__(self,surname,firstname,age,pin,tel_number,account_number,account_balance):
        super.__init__(self,surname,firstname,age,pin,tel_number,account_number,account_balance)

    def createaccount(self):
        con = sqlite3.connect('customers.db')
        cursor = con.cursor()
        try:
            cursor.execute("""CREATE TABLE bank_users (Surname TEXT char(30), Firstname TEXT char(30),
                Age INT n(2) , Pin TEXT char(4) , Tel_number TEXT n(11) , Account_number INT(10) ,
                Account_balance INT n(9) )""")
        except sqlite3.OperationalError:
            Surname = Bank_login.__init__(self.surname)
            Firstname = Bank_login.__init__(self.firstname)
            Age = Bank_login.__init__(self.age)
            Pin = Bank_login.__init__(self.pin)
            Tel_number = Bank_login.__init__(self.tel_number)
            Account_number = Bank_login.__init__(self.account_number)
            Account_balance = Bank_login.__init__(self.account_balance)
            print('   Please wait while we process your request...')
            time.sleep(3.0)
            print(f"""Dear {Firstname} you have successfully created a bank account \n**Here are your account details**
            Account owner = {Surname} {Firstname}
            Account number = {Account_number}
            Pin number = {Pin}
            Account balance = N{Account_balance}""")
            cursor.execute(""" INSERT INTO bank (Surname,Firstname,Age,Pin,Tel_number,Account_number,Account_balance) 
            VALUES (?,?,?,?,?,?,?)
            """,(Surname,Firstname,Age,Pin,Tel_number,Account_number,Account_balance))
            con.commit()
            con.close()

instance = Create_account('surname','firstname','age','pin','tel_number','account_number','account_balance')
instance.createaccount()
    
#     def user_input_details(self):
# # class user_input_details():
#         user_account_number = int(input('Enter your account number\n'))
#         pin = int(input('Enter your pin number\n'))
#         while user_account_number not in self.createaccount() and user_account_number not in self.createaccount:
#             print('Sorry you have entered an invalid account number or pin\n')     
#         else:
#             print('You have logged into your bank account')
            
