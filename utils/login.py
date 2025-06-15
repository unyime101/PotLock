from config.db_config import db_con
from .signup import sign_up
def login():
    logged_in = False
    print("*Login time!*")
    while(logged_in == False):#first while loop ensures users must stay and enter all the correct details
        user_exist= False
        while(user_exist == False):#makes sure a valid email is entered
            usr_email = input("Please enter a registered email address: ")
            mydb = db_con()
            crsr =  mydb.cursor()
            query = "SELECT * FROM users WHERE email = %s"
            crsr.execute(query, (usr_email,))
            result = crsr.fetchone()#returns a single entry that matches the username
            mydb.close()
            if(result is None):#if nothing is returned means there isnt a username stored in the db
                ans = input("*ERROR* \n Unfortnunatley that email is not registered with us. Would you like to (1)TRY AGAIN (2) Sign Up: ")#gives user a chacnce to create an account.
                if(ans == "1"):
                    user_exist = False
                else:
                    sign_up()
            else:
                user_exist = True
        print("********************************")
        correct_pass = False
        while(correct_pass == False):
            passwrd = input("Please enter your password:  ")
            mydb = db_con()
            crsr =  mydb.cursor()
            query = "SELECT passw FROM users WHERE email = %s"
            crsr.execute(query, (usr_email,))
            result = crsr.fetchone()#returns passw that matches the username
            mydb.close()
            db_pass = result[0]#fetch one still returns a tuple, just has one val though, so must select the firsrt one in tuple.
            if(db_pass != passwrd):#if the password does not match the stored one for that email
                ans = input("*ERROR* \n Unfortnunatley the account details don't match, incorrect password. Would you like (1)to try again or (2)enter a new email?: ")
                if(ans == "1"):
                    correct_pass = False
                else:
                    user_exist =False
                    break
            else:
                correct_pass = True# allows user to exit the loop
        
        if(user_exist == True and correct_pass== True):
            mydb = db_con()
            crsr =  mydb.cursor()
            query = "SELECT user_id FROM users WHERE email = %s"
            crsr.execute(query, (usr_email,))
            id = crsr.fetchone()[0]#returns userid that matches the username
            mydb.close()
            logged_in = True
    return id
        


    

            
