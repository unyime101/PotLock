from config.db_config import db_con

def active_pots(acc_id):
    mydb = db_con()
    crsr = mydb.cursor()
    query = "select count(*) from pots where account_id = %s" #will select just the number of active pots 
    crsr.execute(query,(acc_id,)) # note mswl still expects a tuple for the place holder
    activePots = crsr.fetchone()[0]
    return activePots

def create_pot(acc_id):
    name= input("Please Provide a name for the Pot you would like to make: ").strip()
    goal_amount =int(input("Please provide your goal ammount youd like to set: ").strip())
    locked_until = input("Please provide a date you would like the savings pot to be reopened. In the format yyyy-mm-dd.").strip()
    print("***************************************************")
    choice = input("Would you like to make a deposit into the pot? (1)Yes (2)No ").strip()
    choice_made = False
    while choice_made ==False:
        if choice == "1":
            current_amount = int(input("Please provide an amount you'd like to deposit: ").strip())
        elif choice == "2":
             current_amount = 0
        else:
          print("please make a choice (1) make a depsit or (2) No deposit yet just make the pot")              
    is_locked = True
    val = (name,goal_amount,current_amount,locked_until,is_locked,acc_id)
    query = "INSERT INTO pots (name, goal_amount, current_amount, locked_until, is_locked,account_id) VALUES (%s, %s, %s, %s, %s,%s)"
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute(query,val)
    mydb.commit()
    mydb.close()

#def deposit_pot(pot_id):
