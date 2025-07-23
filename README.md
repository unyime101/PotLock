# PotLock
# A finances managment system that will automate and simplify saving.
Technologies used so Far: Python, mysql 
This is an original soloution i had and decided to develope it to help myeslf and others manage savings.
Users will have access to an active balance which they can withdraw money from.
Whilst also having "Pots" which act as saving stores which will be locked until either the target amount is reached or end date.
Each pot will haave a "weighting", this will be the percentage of whatever is deposited into the account that will be automatically put into the pot.
For instance. £50 is deposited into the account but the user has a pot of 0.1% weighting. The active balance will be £45 and £5 will be in the pot
The pots will continue to fill. Once the pot is full it will become "live" so the user can make the goal purchae, house, car etc. 
The weighting of the "live" pot is then divided and used for the other active saving pots, in turn increasing their growth.
Will work great for people with constant incomes, for instance i am being paid weekly at my current job.

Key functionalities:
* User Login/sign up
* Deposit into and withdraw from account
* Display: active balance, live saving pots, active pots and log out
* Create Pots 
* Track Pot Progress
* Edit user details 


Current progress notes:
* Login,signup created.
* Deposit,Account details views created.
* Working on Pots!!!!, Pot view created. And Pot creation ready to be implemented. Will also need to create verification meth for new pots.

Potential further developments: 
* Creating a better UI
* Looking into deploying and learning kubernetes with it