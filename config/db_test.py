from db_config import db_con #correct file path allowing me to accces meth in db con

def get_tables():#Testing connection 
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute("Show TABLES")
    tables = crsr.fetchall()
    for table in tables:
        print(table[0])
    mydb.close()

def get_users():#outputs all users and their details stored in usrs table
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute("Select * from users")
    users = crsr.fetchall()
    for users in users:
        print (users)
    mydb.close()


def get_accounts():#outputs all accounts and their details stored in usrs table
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute("Select * from accounts")
    accounts = crsr.fetchall()
    for accounts in accounts:
        print(accounts[0])
    mydb.close()


def get_pots():#outputs all pots and their details stored in usrs table
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute("Select * from pots")
    pots = crsr.fetchall()
    for pots in pots:
        print(pots[0])
    mydb.close()
    


def account_det():
    act_balance = 9999
    user_id = 15
    mydb = db_con()
    crsr = mydb.cursor()
    query = "INSERT INTO accounts (active_balance, user_id) VALUES (%s, %s)"# no. of %s must match no. of inputs
    val = (act_balance, user_id)#accepts type tuple
    crsr.execute(query, val)
    mydb.commit()
    mydb.close()



#active_pots(acc_id):
mydb = db_con()
crsr = mydb.cursor()
acc_id =1
query = "select count(*) from pots where account_id = %s" #will select just the number of active pots 
crsr.execute(query,(acc_id,)) # note mswl still expects a tuple for the place holder
activePots = crsr.fetchone()[0]
if activePots>0:
    print (activePots)
elif activePots==0:
    print("no pots")
else:
    print("null probanbly returned")

    