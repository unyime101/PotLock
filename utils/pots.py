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
    choice_made = False
    while choice_made ==False:
        choice = input("Would you like to make a deposit into the pot? (1)Yes (2)No ").strip()#ensures a choice is made before moving on
        if choice == "1":
            current_amount = int(input("Please provide an amount you'd like to deposit: ").strip())
            if current_amount<=goal_amount:
                choice_made = True
            else:
                print("The amount you are depositing into the pot must be less than or equal to the goal amount!")
                choice = False
        elif choice == "2":
            current_amount = 0
            choice_made = True
        else:
            print("please make a choice (1) make a depsit or (2) No deposit yet just make the pot") 
    format = False
    while format == False:#ensures all inputs are correct and follow logic of the program.
        weighting = int(input("Please provide a weighting for this pot.\n Note weighting refers to the percentage of your deposits/ income that goes into this pot. \n 30""% Weighting is 30 perecent of your income will go into this account ").strip())
        print("\033[34m*************************************\033[0m")
        if weighting.is_integer and int(weighting)<=100:
            valid = valid_weight(acc_id,weighting)
            if valid == True:
                format = True
            else:
                format = False    
        else:
            print("Not a valid input try again. Please ensure youve entered a digit that is also less than or equal to the weighting you have available.")
            print("\033[34m*************************************\033[0m")
    is_locked = True
    val = (name,goal_amount,current_amount,locked_until,is_locked,acc_id,weighting)
    query = "INSERT INTO pots (name, goal_amount, current_amount, locked_until, is_locked,account_id, weighting) VALUES (%s, %s, %s, %s, %s,%s,%s)"
    print("******************************** \n\033[32mPot Created Successfully! Please refesh on return to main menu.\033[0m \n******************************** ")
    mydb = db_con()
    crsr = mydb.cursor()
    crsr.execute(query,val)
    mydb.commit()
    mydb.close()
    #apply a collateral procedure, ask the user to add a ranking. High, med, low to each pot. 
    #Once the pot has been closed/completed the weighting added to next highest priority pot the user has
    #Will incremently increase the growth of pots as the user continues to deposit, encouraging the to keep saving.
    # collateral will increase over time the more pots they have the greater the growth as the complete them

def display_act_pots(acc_id):
    query = "Select name, goal_amount, current_amount, locked_until, is_locked, weighting from pots where account_id = %s and is_locked = %s"
    mydb = db_con()
    crsr = mydb.cursor()
    val = 1
    crsr.execute(query,(acc_id,val))
    pots = crsr.fetchall()
    if pots :
            for i in pots:
                pot_name =i[0]# iterates through returned val from db
                pot_goal = i[1]
                pot_balance = i[2]
                locked_until = i[3]
                pot_weight = i[5]
                print("\033[34m*************************************\033[0m")
                print("\033[31m",pot_name,"\033[0m""\n\033[32mPot Goal:\033[0m",pot_goal,"\n\033[32mPot Current Balance:\033[0m",pot_balance,"\n\033[31mPot Access Date:\033[0m",locked_until,"\n\033[32mPot Weight of Pot:\033[0m",pot_weight,"" )
                print("\033[34m*************************************\033[0m \n\033[34m*************************************\033[0m ")    
    else:
        print("You have no active pots, please create one!")

    mydb.close()

def display_comp_pots(acc_id):
    query = "Select name, goal_amount, current_amount, locked_until, is_locked, weighting from pots where account_id = %s and is_locked= %s"
    mydb = db_con()
    crsr = mydb.cursor()
    val = 0
    crsr.execute(query,(acc_id,val))
    pots = crsr.fetchall()
    if pots :
            for i in pots:
                pot_name =i[0]# iterates through returned val from db
                pot_goal = i[1]
                pot_balance = i[2]
                locked_until = i[3]
                pot_weight = i[5]
                print("\033[34m*************************************\033[0m")
                print("\033[31m",pot_name,"\033[0m""\n\033[32mPot Goal:\033[0m",pot_goal,"\n\033[32mPot Current Balance:\033[0m",pot_balance,"\n\033[31mPot Access Date:\033[0m",locked_until,"\n\033[32mPot Weight of Pot:\033[0m",pot_weight,"" )
                print("\033[34m*************************************\033[0m \n\033[34m*************************************\033[0m ")    
    else:
        print("You have no completed pots, get to saving!")
    mydb.close()


def valid_weight(acc_id, pot_weight):#will check that on creating new pots the weighting of their income being put in makes sense. i.e total amount of weight per acc
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
    if (current_total+pot_weight) > 100:#checks if youre able to add the weight of this pot without surpasing 100%
        print("Unfortunately you cannot make a pot of",pot_weight,"% Weighting.\n You have\033[31m",perc_left,"\033[0m% Available to use")
        validation = False
    elif(current_total+pot_weight)== 100:
        while choice_made == False:
            choice =input("Please note you will be using up the last of your available pot weighting. Do you still wish to continue? (1)Yes (2)No:")
            if choice.strip() == "1":
                print("Okay validating.")
                validation = True
                choice_made = True
            elif choice.strip() =="2":
                print("Understood. Validation incomplete please select a new weighting, less than",perc_left,"")
                validation = False
                choice_made = True
            else:
                print("Please enter a valid input. (1)Yes(2)No.")
    else:
        print("validation complete successfully!")
        validation = True
    return validation
#def deposit_pot(pot_id):
