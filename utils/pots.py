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
    #apply a collateral procedure, ask the user to add a ranking. High, med, low to each pot. 
    #Once the pot has been closed/completed the weighting added to next highest priority pot the user has
    #Will incremently increase the growth of pots as the user continues to deposit, encouraging the to keep saving.
    # collateral will increase over time the more pots they have the greater the growth as the complete them

def display_pots(activepots,acc_id):
    query = "Select name, goal_amount, current_amount, locked_until, is_locked, weighting from pots where account_id = %s"
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute(query,(acc_id,))
    pots = str(crsr.fetchall())
    print("Hey you have",activepots," active pots. See below: ", pots)
    mydb.close()


#def deposit_pot(pot_id):
