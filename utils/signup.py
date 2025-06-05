from config.db_config import db_con

def sign_up():
    valid_fields =False
    email = input("Please enter your email address, this will act as your login user name: ").strip()
    Name = input("Please enter your full name: ").strip()
    phonenumber = input("Please enter your phone number: ").strip()
    passw = input("Please enter a password: ").strip()    
    while(valid_fields ==False):#while loop to ensure user cannot progress until the fields are filled in the correct format

        if not email.strip(): #strip will remove whitespaces. Strip will return bool. If empty returns false. not operation flips therefore being true and message shown 
            email = input("**ERROR** \n Please enter an Email address: ")
        elif not Name.strip():
            Name = input("**ERROR** \n Please enter your full Name : ")
        elif (not phonenumber.strip()) or (not phonenumber.isdigit()) :# also checking if the input is of int val as all phone numvbers should be
            phonenumber = input("**ERROR** \n Please enter your Phone Number: ")
        elif not passw.strip():
            passw= input("**ERROR** \n Please enter a Password: ")
    
        else:#if none of these checks are triggerd it will break and move onto the sign up like normal
            valid_fields = True
    try:# try catch so the program doesnt halt even i the event of an error.
        mydb = db_con()#makes use of meth created in dbconfig with all database pass 
        crsr = mydb.cursor()# cursor created
        query = "INSERT INTO users (name, email, passw, phonenumber) VALUES (%s, %s, %s, %s)"# no. of %s must match no. of inputs
        val = (Name, email, passw, phonenumber)#accepts type tuple
        crsr.execute(query, val)
        mydb.commit()
        print("Congrats and Welcome to Pot Lock, Excited to begin this saving journey with you!")
    except Exception as e:
        print(" Insert failed:", e)
    finally:
        mydb.close()
