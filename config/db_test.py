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

acc_id = 7
name= input("Please Provide a name for the Pot you would like to make: ").strip()
goal_amount =int(input("Please provide your goal ammount youd like to set: ").strip())
locked_until = input("Please provide a date you would like the savings pot to be reopened. In the format yyyy-mm-dd.").strip()
print("***************************************************")
choice = input("Would you like to make a deposit into the pot? (1)Yes (2)No ").strip()#ensures a choice is made before moving on
choice_made = False
while choice_made ==False:
    if choice == "1":
        current_amount = int(input("Please provide an amount you'd like to deposit: ").strip())
        choice_made = True
    elif choice == "2":
        current_amount = 0
        choice_made = True
    else:
        print("please make a choice (1) make a depsit or (2) No deposit yet just make the pot") 
    format = False
    while format == False:#ensures all inputs are correct and follow logic of the program.
        weighting = int(input("Please provide a weighting for this pot.\n Note weighting refers to the percentage of your deposits/ income that goes into this pot. \n 30""% Weighting is 30 perecent of your income will go into this account ").strip())
        if weighting.is_integer and int(weighting)<=100:
            format = True
        else:
            print("Not a valid input try again. Please ensure youve entered a digit that is also less than or equal to 100.")
    is_locked = True
    val = (name,goal_amount,current_amount,locked_until,is_locked,acc_id,weighting)
    query = "INSERT INTO pots (name, goal_amount, current_amount, locked_until, is_locked,account_id, weighting) VALUES (%s, %s, %s, %s, %s,%s,%s)"
    print("******************************** \n******************************** \n******************************** \n******************************** \n******************************** ")
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute(query,val)
    mydb.commit()
    mydb.close()