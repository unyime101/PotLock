from config.db_config import db_con

def acccountDetails(usr_id):
    mydb = db_con()
    crsr =mydb.cursor()
    query1 = "Select name from user Where user_id = %s"
    query2 = "Select active_balance from account Where user_id = %s"
    val = usr_id
    crsr.execute(query1,(val,))
    name = crsr.fetchone()
    crsr.execute(query2,(val,))
    active_balance = crsr.fetchone()
    mydb.close()

    



