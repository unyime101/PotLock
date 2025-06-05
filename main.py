from utils.signup import sign_up
from config.db_test import get_users, get_tables
from utils.login import login
 
#get_tables()
usr_id = login()# will be used further to select all user details linked to this id
print(usr_id)
#sign_up()
#get_users()