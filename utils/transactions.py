from config.db_config import db_con
def deposit(user_id, active_balance ):# will take the amount and update the database with the vals. depending on how may pots and thos pots weight
    income = input("How much Would you like to deposit? ").strip()
    up_act_balance = float(active_balance) +float(income)# just a dummy calc
    mydb = db_con()
    crsr = mydb.cursor()
    query = "UPDATE accounts SET active_balance = %s where user_id = %s"
    vals = (up_act_balance, user_id)
    crsr.execute(query, vals)
    mydb.commit()
    mydb.close()
    print(up_act_balance)