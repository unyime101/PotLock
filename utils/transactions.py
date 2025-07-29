from config.db_config import db_con
from pots import active_pots, fetch_pots
def deposit(acc_id, active_balance ):# will take the amount and update the database with the vals. depending on how may pots and thos pots weight
    val = active_pots(acc_id)
    income = input("How much Would you like to deposit? ").strip()
    if val>0:
        locked = 1
        stream = fetch_pots(acc_id,locked)
        i =0
        left_over = 0
        while i < val:
            current_pot_id = stream[i][1]
            current_pot_balance = stream[i][2]
            current_pot_weight = (stream[i][3])/100#prepares percentage for cals
            new_pot_balance = current_pot_balance + (income * current_pot_weight)#calcs for updating pot 
            if left_over != 0:
                new_pot_balance + (left_over*current_pot_weight)
            if new_pot_balance > current_pot_balance:#check to see if the pot has been filled
                print("congrats you have filled Pot:",stream[i][0],"")
                left_over = new_pot_balance-current_pot_balance
                locked = 0
            elif new_pot_balance == current_pot_balance:
                print("congrats you have filled Pot:",stream[i][0],"")
                locked = 0
            else:
                left_over = 0
                locked = 1

    
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
    

 


    
