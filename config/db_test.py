from .db_config import db_con #correct file path allowing me to accces meth in db con

def get_tables():#Testing connection 
    con = db_con()
    cursor = con.cursor()
    cursor.execute("Show TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    con.close()

def get_users():#outputs all users and their details stored in usrs table
    mydb = db_con()
    cursor = mydb.cursor()
    cursor.execute("Select * from users")
    users = cursor.fetchall()
    for users in users:
        print (users)
    mydb.close()


def get_accounts():#outputs all accounts and their details stored in usrs table
    mydb = db_con()
    cursor = mydb.cursor()
    cursor.execute("Select * from accounts")
    accounts = cursor.fetchall()
    for accounts in accounts:
        print(accounts[0])
    mydb.close()


def get_pots():#outputs all pots and their details stored in usrs table
    mydb = db_con()
    cursor = mydb.cursor()
    cursor.execute("Select * from pots")
    pots = cursor.fetchall()
    for pots in pots:
        print(pots[0])
    mydb.close()


