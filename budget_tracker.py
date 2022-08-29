"""
Why: keep track of my expenses, savings, and wants
    - Used to see if I can afford things or not
    - Used to help plan bills payments better
    - Used to make better financial decisions
"""

consent = True
while consent == True:   # asking the user for consent on if they're willing to enter private financial information
    ask_consent = input("""To start, we will need to ask for a few information regarding your finances.
    If that is okay and you wish to continue enter 'y'. If not, enter 'n': """).lower()
    if ask_consent == 'y':
        consent = False   # used so that it doesn't get asked again after approval
        break
    elif ask_consent == 'n':
        print("Thank you for using our service, please come again.")
        exit()
    else:
        print("Invalid input. Try again.")
        continue

# dictionary that holds the users income info
inc_info = {}
inc_total = sum(inc_info.values())

# dictionary that holds the users expense info
exp_info = {}
exp_total = sum(exp_info.values())

# dictionary that holds the users budget plan information
budget_plan = {
    'expenses' : 50,
    'wants' : 30,
    'savings' : 20
}
budget_info = {
    'exp_plan' : int(inc_total * (budget_plan['expenses'] / 100)),
    'want_plan' : int(inc_total * (budget_plan['wants'] / 100)),
    'save_plan' : int(inc_total * (budget_plan['savings'] / 100))
}

# this function adds new entries to specific dictionaries
def add_to(aDict):
    """
    aDict: any dictionary to add to
    name_of: a string, just used to print the name of the dictionary being interacted with
    """
    add_name = input("What would you like to enter: ")
    add_amount = input("What is the amount of the item: ")
    aDict[add_name.lower()] = int(add_amount)

# this function deletes a key-value pair from a dictionary
def del_from(aDict):
    """
    aDict: any dictionary to delete from
    name_of: a string, just used to print the name of the dictionary being interacted with
    """
    while True:
        print(aDict)
        del_name = input("Which item would you like to delete ('q' to quit)? Enter name: ").lower()
        if del_name == 'q':
            break
        elif del_name in aDict:
            del_confirm = input("Are you sure you want to delete " + del_name + "? y/n: ").lower()
            if del_confirm == 'y':
                del aDict[del_name]
                print(del_name + " was successfully deleted.")
                continue
            elif del_confirm == 'n':
                print(del_name + " will not be deleted.")
                continue
            else:
                print("Invalid input.")
            del_more = input("Would you like to delete another item? y/n: ")
            if del_more == 'y':
                continue
            elif del_more == 'n':
                break
            else:
                print("Invalid input.")
                continue   # send the user back to the top of the while loop
        else:
            ask_again = input("We don't see that value. Would you like to try again? y/n: ").lower()
            if ask_again == 'y':
                continue
            elif ask_again == 'n':
                break
            else:
                print("Invalid input.")
                continue   # send the user back to the top of the while loop

# this function modifies the value of an already existing item in a dictionary
def mod_amount(aDict):
    """
    aDict: the dictionary with the item's value being changed
    """
    while True:
        print(aDict)
        to_mod = input("Which item's value would you like to change ('q' to quit)? ")
        if to_mod == 'q':
            print("Going back to the main page.")
            break
        elif to_mod in aDict:
            mod_val = int(input("What is the item's new amount? "))
            mod_confirm = input("Are you sure you want to change the value? y/n: ").lower()
            if mod_confirm == 'y':
                aDict[to_mod] = mod_val
                print(aDict[to_mod])
                print("The item's value was successfully changed")
            elif mod_confirm == 'n':
                print("The value will not be changed.")
                continue
            else:
                print("Invalid input. Try again.")
                continue
        elif to_mod not in aDict:
            print("That item was not found. Please try again.")
            continue
        else:
            print("Invalid input. Try again.")
            continue

# this function allows the user to view specific dictionaries
def view_dict(aDict, name_of):
    """
    aDict: any dictionary the user would like to view
    name_of: just used to display the name of the dictionary being accessed
    """
    print("Currently Viewing: " + name_of)
    for key, value in aDict.items():
        print(key + " : " + str(value))

# this function allows the user to change their budget plan
def change_plan(bp):
    """
    bp: the budget plan dictionary
    """
    print("Note: the new budget plan must equal to 100.")
    while True:
        new_expense = int(input("How much would you like to allocate towards expenses? "))
        new_wants = int(input("How much would you like to allocate towards wants? "))
        new_savings = int(input("How much would you like to allocate towards savings? "))
        new_total = new_expense + new_wants + new_savings
        if new_total != 100:
            print("Those number's don't add up to 100, please try again.")
            continue
        elif new_total == 100:
            double_check = input("Your new budget plan is about to be saved, are you sure you want to confirm? y/n: ").lower()
            if double_check == 'y':
                bp['expenses'] = new_expense
                bp['wants'] = new_wants
                bp['savings'] = new_savings
                print(bp)
                print("Your new budget plan was successfully saved.")
                break
            elif double_check == 'n':
                print("The changes will not be made, you may try again.")
                continue
            else:
                print("Invalid input, please try again.")
                continue
        else:
            print("Invalid input, please try again.")
            continue

# this function shows the user a recommended budget allocation amount
def rec_exp(d1, d2):
    d1_values = d1.values()
    d1_total = sum(d1_values)
    d2_values = d2.values()
    d2_total = sum(d2_values)
    recommended_ratio = int((d1_total / d2_total) * 100)
    print("Based on your financial standing, the recommended expense allocation ratio is: " + str(recommended_ratio) + ".")

# this function tells the user what range percentage their 'want' falls under
def want_this():
    want_val = int((budget_plan['wants'] / 100) * inc_total)
    what_u_want = int(input("How much does the 'want' cost? "))
    want_dict = {   # playing with dictionaries
        '20' : int(want_val / 20),
        '40' : int(want_val / 40),
        '60' : int(want_val / 60),
        '80' : int(want_val / 80),
        '100' : int(want_val)
    }
    if what_u_want <= want_dict['20']:
        print("This 'want' is within the 20 percent range for your tolerable wants budget.")
    elif want_dict['20'] < what_u_want <= want_dict['40']:
        print("This 'want' is within the 20 to 40 percent range for your tolerable wants budget.")
    elif want_dict['40'] < what_u_want <= want_dict['60']:
        print("This 'want' is within the 40 to 60 percent range for your tolerable wants budget.")
    elif want_dict['60'] < what_u_want <= want_dict['80']:
        print("This 'want' is within the 60 to 80 percent range for your tolerable wants budget.")
    elif want_dict['80'] < what_u_want <= want_dict['100']:
        print("This 'want' is within the 80 to 100 percent range for your tolerable wants budget.")
    elif want_dict['100'] < what_u_want:
        print("This 'want' surpasses your tolerable monthly wants budget.")
    else:
        print("Invalid input.")

# this function allows the user to set a save plan with a target goal and monthly timeframe
def save_plan():
    save_goal = int(input("How much money would you like to save? "))
    save_time = int(input("In how many months do you need it? "))
    save_per_month = int(save_goal / save_time)
    save_plan = float((save_per_month / inc_total) * 100)
    print("In order to save $" + str(save_goal) + " in " + str(save_time) + " month(s), you would need to save $" + str(save_per_month))
    print("This means you would need to allocate at least " + str((round(save_plan, 2))) + " for your 'savings' budget.")
    print("Your current savings allocation is: " + str(budget_plan['savings']))

# this function allows the user to play with the dictionaries to 
def budget_play(aDict, type):
    """
    aDict: dictionary being played with
    type: 'inc' or 'exp' just used for the status report section of the function
    """
    copy_dict = aDict.copy()
    while True:
        print(copy_dict)
        options = input("What would you like to do? add(a), delete(d), update(u), restart(r), status(s), quit(q)? ").lower()
        if options == 'q':
            break
        elif options == 'a':
            add_to(copy_dict)
            continue
        elif options == 'd':
            del_from(copy_dict)
            continue
        elif options == 'u':
            mod_amount(copy_dict)
            continue
        elif options == 'r':
            copy_dict = aDict.copy()
            continue
        elif options == 's':
            copy_sum = int(sum(copy_dict.values()))
            if type == 'inc':
                copy_sum_exp = int((exp_total / copy_sum) * 100)
                print("Your new income would be: " + str(copy_sum))
                print("Your new tolerable expense budget would be: " + str(copy_sum_exp))
            else:   # type == 'exp'
                copy_sum_inc = int((copy_sum / inc_total) * 100)
                print("Your new expense would be: " + str(copy_sum))
                print("Your new tolerable expense budget would be: " + str(copy_sum_inc))
        else:
            print("Invalid input.")
            continue

# Terminal interface that the user will interact with
while True:
    print("""
    Sections Menu:
    1. Modify Budget Information
    2. Budget Analysis
    3. Budget Play
    4. View Budget
    Enter 'v' to view all actions within each section.
    Enter 'q' to quit.
    """)

    choice = input("What section would you like to choose? Enter number: ")

    if choice == 'q' or 'Q':
        print("Thank you for using our service. Come again!")
        exit()

    elif choice == 'v' or 'V':
        print("""
        1. Modify Budget Information
            a. Modify income
            b. Modify expenses
            c. Modify savings goal
        2. Budget Analysis
            d. Recommended income
            e. Recommended expense
            f. Wants analysis
        3. Budget Play
            g. Play with different budget rules
            h. Play with current expenses
            i. Play with current income
        4. View Budget
            j. View all budget information
            k. View all expense information
            l. View all income information
            m. View all wants information
        """)

    elif choice == '1':
        print("""
        a. Modify income (fixed and variable)
        b. Modify expenses (fixed and variable)
        c. Modify savings goal
        """)
        
    elif choice == '2':
        print("""
        d. Recommended income
        e. Recommended expense
        f. Wants analysis
        """)
        
    elif choice == '3':
        print("""
        g. Play with different budget rules
        h. Play with current expenses
        i. Play with current income
        """)
        
    elif choice == '4':
        print("""
        j. View all budget information
        k. View all expense information
        l. View all income information
        m. View all wants information
        """)
        
    else:
        try_again = input("Invalid input. Would you like to try again? y/n: ")
        if try_again == "y":
            continue
        elif try_again == "n":
            print("Thank you for using our service. Come again!")
            exit()
        else:
            print("Bro.")
            exit()

