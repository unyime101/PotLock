from utils.signup import sign_up
from config.db_test import get_users, get_tables
from utils.login import login
choice = False
usr_id=0
print("Hello, welcome to PotLock! A savings and finances management system. Saving made easy, No luck needed. \n************************************************************** ")
while(choice == False):
    x = input("Are you a new user or reuturning? \n (1) Sign up (2) Sign In: ")
    if(x.strip() == "1"):
        sign_up()
        usr_id = login()
        choice=True
    elif(x.strip()=="2"):
        usr_id = login()# will be used further to select all user details linked to this id
        choice=True
    else:
        print("*ERROR** \n Please make a choice by entering the number 1 or 2 \n **********************************")
#Display current balance and active pots
# Choice to (1) deposit (2)manage pots (3)manage account details 

#  print(usr_id)



#sign_up()
