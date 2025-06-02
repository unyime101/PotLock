from config.db_config import db_con
def login():
    print("*Login time!*")
    usrname = input("Please enter your email address: ")
    user_exist= False
    while(user_exist == False):
        mydb = db_con()
        crsr =  mydb.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        crsr.execute(query, (usrname,))
        result = crsr.fetchone()#
        mydb.close()
        if(result is not None):
            usrname = input("*ERROR* \n Unfortnunatley that email is not registered with us. Would you like to (1)TRY AGAIN (2 Sign Up): ")
            if():
        
        else:
