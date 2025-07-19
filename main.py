from utils.signup import sign_up
from config.db_test import get_users, get_tables, account_det
from utils.login import login
from utils.accounts import acccountDetails, first_deposit
from utils.transactions import deposit

new_user = False
choice = False
usr_id=0
active_balance = 0
print("Hello, welcome to PotLock! A savings and finances management system. Saving made easy, No luck needed. \n************************************************************** ")
while(choice == False):
    x = input("Are you a new user or reuturning? \n (1) Sign up (2) Sign In: ")
    if(x.strip() == "1"):
        sign_up()
        usr_id = login()
        first_deposit(usr_id)# new users must deposit money into the account if theyd like to keep it open
        choice=True
    elif(x.strip()=="2"):
        usr_id = login()# will be used further to select all user details linked to this id
        choice=True
    else:
        print("*ERROR** \n Please make a choice by entering the number 1 or 2 \n **********************************")
#Display current balance and active pots

active_balance = acccountDetails(usr_id)# current balance completed. Active pots needs to be done after pots made
#work on active pots

# Choice to (1) deposit (2)manage pots (3)manage account details (3)refresh  (4) None Sign out
action = False
while(action == False):
    x = input("(1)Make a Deposit (2)Manage pots (3)Manage account details (4)Refresh  (5)None Sign out ")
    if(x.strip() == "1"):
        deposit(usr_id,active_balance)
        acccountDetails(usr_id)
    elif(x.strip()=="2"):#will display active pots and allow the user to access each individual pot
        print("Pots currently in use: \n **working on**")
    elif(x.strip()=="3"):
        print("Account details.... Which would you like to update: \n **working on**")
    elif(x.strip()=="4"):
        acccountDetails(usr_id)
    elif(x.strip()=="5"):
        usr_id = 0
        action = True
    else:
        print("*ERROR** \n Please make a choice by entering the numbers, 1,2,3,4,5 \n **********************************")
print("Succesfully logged out. ")




