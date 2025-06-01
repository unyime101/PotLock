from config.db_config import db_con

def sign_up():
    email = input("Please enter your email address: ")
    Name = input("Please enter your full name: ")
    phonenumber = input("Please enter your phone number: ")
    passw = input("Please enter a password: ")

    try:
        mydb = db_con()#makes use of meth created in dbconfig with all database pass 
        crsr = mydb.cursor()# cursor created
        query = "INSERT INTO users (name, email, passw, phonenumber) VALUES (%s, %s, %s, %s)"# no. of %s must match no. of inputs
        val = (Name, email, passw, phonenumber)#accepts type tuple
        crsr.execute(query, val)
        mydb.commit()
        print("Congrats and Welcome to Pot Lock, Excited to begin this saving joirney with you!")
    except Exception as e:
        print(" Insert failed:", e)
    finally:
        mydb.close()
