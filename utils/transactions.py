from config.db_config import db_con
from pots import active_pots
def deposit(acc_id, active_balance ):# will take the amount and update the database with the vals. depending on how may pots and thos pots weight
    val = active_pots(acc_id)
    income = input("How much Would you like to deposit? ").strip()
    if val>0:
        print("Hello")
        #should accurateley split the weighting and update pots
        # will use the fetch pots method
    elif val == 0:
        print("You have no active pots so all your income will go to your active account balance.")
        print("\033[34m*************************************\033[0m")
        up_act_balance = float(active_balance) +float(income)#updates the balance
        mydb = db_con()
        crsr = mydb.cursor()
        query = "UPDATE accounts SET active_balance = %s where account_id = %s"
        vals = (up_act_balance, acc_id)
        crsr.execute(query, vals)
        mydb.commit()
        mydb.close()
    else:
        print("Error!!!")
    

 

def fetch_pots(acc_id):
    query ="Select weighting pot_id, goal_amount from pots where acc_if =%s"
    mydb = db_con()
    crsr = mydb.cursor()
    stream = crsr.execute(query,(acc_id,))
    
