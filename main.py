from utils.signup import sign_up
from utils.login import login
from utils.accounts import acccountDetails,accountID, first_deposit
from utils.transactions import deposit
from utils.pots import display_act_pots,create_pot,display_comp_pots

new_user = False
choice = False
usr_id=0
acc_id=0
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
acc_id = accountID(usr_id)
active_balance = acccountDetails(usr_id,acc_id)# current balance completed. Active pots needs to be done after pots made
# Choice to (1) deposit (2)manage pots (3)manage account details (4)refresh  (5) None Sign out
action = False
while(action == False):
    x = input("(1)Make a Deposit (2)Create New Pot (3)View Active Pots (4)View Completed Pots (5)Manage account details  (6)Refresh (7)None Sign out ")
    if(x.strip() == "1"):
        deposit(acc_id,active_balance)
        acccountDetails(usr_id, acc_id)
    elif(x.strip()=="2"):
        create_pot(acc_id)# create pot method implemented
    elif(x.strip()=="3"):#will display active pots 
        display_act_pots(acc_id)
    elif(x.strip()=="4"):#will display completed pots the user can use 
        display_comp_pots(acc_id)
    elif(x.strip()=="5"):
        print("Account details.... Which would you like to update: \n **working on**")
    elif(x.strip()=="6"):
        acccountDetails(usr_id,acc_id)
    elif(x.strip()=="7"):
        usr_id = 0
        acc_id = 0
        action = True
    else:
        print("*ERROR** \n Please make a choice by entering the numbers, 1,2,3,4,5 \n **********************************")
print("Succesfully logged out. ")




