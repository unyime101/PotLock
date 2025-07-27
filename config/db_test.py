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







acc_id =5


#valid_weight(acc_id, pot_weight):#will check that on creating new pots the weighting of their income being put in makes sense. i.e total amount of weight per acc
    #must sum to 100% for logic
query = "Select weighting from pots where account_id = %s and is_locked = %s "# ensures only the weighting of only the active pots are accounted
mydb = db_con()
crsr =mydb.cursor()
locked = 1
crsr.execute(query,(acc_id,locked))
collective = crsr.fetchall()
current_total = 0
perc_left = 0
validation = True
for pot in collective:#totals all the current weights of pots
        current_total += int(pot[0])
choice_made = False
perc_left = 100 - current_total
if (current_total+500) > 100:#checks if youre able to add the weight of this pot without surpasing 100%
    print("Unfortunately you cannot make a pot of",500,"% Weighting.\n You have\033[31m",perc_left,"\033[0m% Available to use")
    validation = False
elif(current_total+500)== 100:
    while choice_made == False:
        choice =input("Please note you will be using up the last of your available pot weighting. Do you still wish to continue? (1)Yes (2)No:")
        if choice == 1:
            print("Okay validating.")
            validation = True
            choice_made = True
        elif choice ==2:
            print("Understood. Validation incomplete please select a new weighting, less than",perc_left,"")
            validation = False
            choice_made = True
        else:
            print("Please enter a valid input. (1)Yes(2)No.")
else:
    print(collective)
    print(current_total)
    print(perc_left)
    print("validation complete successfully!")
    validation = True