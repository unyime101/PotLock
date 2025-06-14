from config.db_config import db_con

def acccountDetails(usr_id):# fetches and displays the account balance, and amount of active saving pots
    mydb = db_con()
    crsr =mydb.cursor()
    query1 = "Select name from users Where user_id = %s"
    query2 = "Select active_balance from accounts Where user_id = %s"
    query3 = "Select account_id from accounts Where user_id = %s"

    crsr.execute(query1,(usr_id,))
    name = crsr.fetchone()[0]
    crsr.execute(query2,(usr_id,))
    active_balance = crsr.fetchone()[0]
    crsr.execute(query3,(usr_id,))
    acc_id =crsr.fetchone()[0]
    mydb.close()
    print("******************************************************************\n******************************************************************")
    print("Hello and welcome," ,name, ". Your Account balance is:", active_balance, ". acc_id =", acc_id,"" )#will leave as this, will further display acctive pots


def first_deposit(user_id):#deposit money into an account
    act_balance = input("How much Would you like to deposit? ").strip()
    mydb = db_con()
    crsr = mydb.cursor()
    query = "INSERT INTO accounts (active_balance, user_id) VALUES (%s, %s)"# no. of %s must match no. of inputs
    val = (act_balance, user_id)#accepts type tuple
    crsr.execute(query, val)
    mydb.commit()
    mydb.close()

def deposit(user_id, active_balance ):# will take the amount and update the database with the vals. depending on how may pots and thos pots weight
    income = input("How much Would you like to deposit? ").strip()
    up_act_balance = active_balance+( income - (income*0.03))# just a dummy calc
    mydb = db_con()
    crsr = mydb.cursor()
    query = ""
    val = (user_id, up_act_balance)
    mydb.commit()
    mydb.close()