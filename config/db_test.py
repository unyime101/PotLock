from db_config import db_con #correct file path allowing me to accces meth in db con
#from utils.pots import active_pots, fetch_pots
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
acc_id = 5
active_balance = 5023.00

def active_pots(acc_id):
    mydb = db_con()
    crsr = mydb.cursor()
    query = "select count(*) from pots where account_id = %s" #will select just the number of active pots 
    crsr.execute(query,(acc_id,)) # note mswl still expects a tuple for the place holder
    activePots = crsr.fetchone()[0]
    return activePots

def fetch_pots(acc_id,locked):
    query ="Select pot_id,name, goal_amount,current_amount,weighting from pots where account_id =%s and is_locked=%s"
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute(query,(acc_id,locked))
    stream = crsr.fetchall()
    return stream




























val = active_pots(acc_id)
income = float(input("How much Would you like to deposit? ").strip())
mydb = db_con()
crsr = mydb.cursor()
query1 = "UPDATE accounts SET active_balance = %s where account_id = %s"
if val>0:
    locked = 1
    stream = fetch_pots(acc_id,locked)
    i =0
    left_over = 0
    total_pot_weight= 0
    while i < val:
        if i>0:
            total_pot_weight +=current_pot_weight#keeps track of pot weights 
        current_pot_id = int(stream[i][0])
        current_pot_goal = float(stream[i][2])
        current_pot_balance = float(stream[i][3])
        current_pot_weight = (stream[i][4])/100#prepares percentage for cals
        new_pot_balance = current_pot_balance + (income * current_pot_weight)#calcs for updating pot 
        if left_over != 0:
            new_pot_balance += (left_over*current_pot_weight)
        if new_pot_balance > current_pot_goal:#check to see if the pot has been filled
            print("congrats you have filled Pot:",stream[i][1],"")
            left_over = new_pot_balance-current_pot_goal#any remainder is stored so it can be divided up again between the pots. "Water fall"
            new_pot_balance = current_pot_goal#ensures the goal is met.
            locked = 0
        elif new_pot_balance == current_pot_balance:
            print("congrats you have filled Pot:",stream[i][1],"")
            new_pot_balance = current_pot_goal#ensures the goal is met.
            left_over = 0
            locked = 0
        elif new_pot_balance<current_pot_goal:
                left_over = 0
                locked = 1
            
        query2 = "UPDATE pots Set current_amount =%s where pot_id=%s "
        crsr.execute(query2,(new_pot_balance,current_pot_id))
        mydb.commit()
        i+=1
    vals = income *(1-total_pot_weight)#works out how much of the income to then put into the active balance
    crsr.execute(query1,(vals,acc_id))
    mydb.commit()
    mydb.close()
    i+=1
    
        #should accurateley split the weighting and update pots
        # will use the fetch pots method
elif val == 0:
    print("You have no active pots so all your income will go to your active account balance.")
    print("\033[34m*************************************\033[0m")
    up_act_balance = float(active_balance) +float(income)#updates the balance
    vals = (up_act_balance, acc_id)
    crsr.execute(query1, (vals,acc_id))
    mydb.commit()
    mydb.close()
else:
    print("Error!!!")
    