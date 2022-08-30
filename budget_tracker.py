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
    print(aDict)
    while True:
        add_name = str(input("What would you like to enter (q to quit): ")).lower()
        if add_name == 'q':
            break
        else:
            add_amount = int(input("What is the amount of the item: "))
            print(add_name + " : " + str(add_amount))
            add_confirm = input("Do you wish to confirm this entry? y/n: ").lower()
            if add_confirm == 'y':
                aDict[add_name.lower()] = int(add_amount)
                print(aDict)
                print("Item successfully added.")
            elif add_confirm == 'n':
                print("Item will not be added.")
                continue
            else:
                print("Invalid input, try again.")
                continue


# this function deletes a key-value pair from a dictionary
def del_from(aDict):
    """
    aDict: any dictionary to delete from
    name_of: a string, just used to print the name of the dictionary being interacted with
    """
    while True:
        print(aDict)
        del_name = input("Which item would you like to delete (q to quit)? Enter name: ").lower()
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
        to_mod = input("Which item's value would you like to change (q to quit)? ")
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


# this function allows the user to view specific dictionaries
def view_dict(aDict, name_of):
    """
    aDict: any dictionary the user would like to view
    name_of: just used to display the name of the dictionary being accessed
    """
    print("Currently Viewing: " + name_of)

    for key, value in aDict.items():
        print(key + " : " + str(value))


# this function shows the user a recommended income for their current financial situation
def rec_inc():
    actual_ratio = int((exp_total / inc_total) * 100)
    plan_ratio = budget_plan['expenses']
    needed_inc = int(exp_total / (plan_ratio / 100))

    print("Actual Expense to Income Ratio: " + str(actual_ratio))
    print("Budget Plan Expence to Income Ratio: " + str(plan_ratio))
    print("Current income: $" + str(inc_total))
    print("Needed income: $" + str(needed_inc))

    if actual_ratio == plan_ratio:
        print("Your actual ratio is equal to your expense plan, this means you do not need to change your income.")
    elif actual_ratio < plan_ratio:
        print("Your actual ratio is BELOW your expense plan, this means that you may have enough income to compensate expenses.")
    else:
        print("Your actual ratio is ABOVE your expense plan, this means that you would need to increase your income.")
        print("You would need to make at least: $" + str(needed_inc) + ", to meet your expense plan.")


# this function shows the user a recommended expense for their current financial situation
def rec_exp():
    actual_ratio = int((exp_total / inc_total) * 100)
    plan_ratio = budget_plan['expenses']
    needed_exp = int(inc_total * (plan_ratio / 100))

    print("Actual Expense to Income Ratio: " + str(actual_ratio))
    print("Budget Plan Expence to Income Ratio: " + str(plan_ratio))
    print("Current expenses: $" + str(exp_total))
    print("Needed expense: $" + str(needed_exp))

    if actual_ratio == plan_ratio:
        print("Your actual ratio is equal to your expense plan, this means you do not need to change your expenses.")
    elif actual_ratio < plan_ratio:
        print("Your actual ratio is BELOW your expense plan, this means you have more than enough income to compensate expenses.")
    else:
        print("Your actual ratio is ABOVE your expense plan, this means that you would need to decrease your expenses.")
        print("Your expenses would need to be at most: $" + str(needed_exp) + ", to meet your expense plan.")


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


# Setting initial values for the income, expense, and budget plan
initial_set = True
while initial_set == True:
    print("Now we are going to ask for some information regarding your finances.")
    print("First we are going to enter your income information.")
    add_to(inc_info)

    print("Now we are going to enter your expense information.")
    add_to(exp_info)

    while True:
        print("Finally, we are going to enter your budget plan preference.")
        print("Note: the default budget plan is: expenses-50, wants-30, savings-20.")
        budget_set = input("Would you like to keep the default budget plan? y/n: ").lower()
        if budget_set == 'y':
            break
        elif budget_set == 'n':
            change_plan(budget_plan)
        else:
            print("Invalid input.")
            continue

    print("Income Info: " + str(inc_info))
    print("Expense Info: " + str(exp_info))
    print("Budget Plan: " + str(budget_plan))

    full_confirm = input("Are you happy with the current information (you may make edits later)? y/n: ")

    if full_confirm == 'y':
        initial_set = False   # This is so that this prompt isn't asked again
        break
    elif full_confirm == 'n':
        continue
    else:
        print("Invalid input.")
        continue


# Terminal interface that the user will interact with
while True:
    print("""
    Sections Menu:
    1. Modify Information
    2. Budget Analysis
    3. Budget Play
    4. View Information
    Enter 'v' to view all actions within each section.
    Enter 'q' to quit.
    """)

    choice = str(input("What section would you like to choose? Enter number: ")).lower()

    if choice == 'q':
        print("Thank you for using our service. Come again!")
        exit()

    elif choice == 'v':
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
            g. Play with current expenses
            h. Play with current income
        4. View Budget
            i. View all budget information
            j. View all expense information
            k. View all income information
            l. View all information
        """)


    elif choice == '1':
        print("""
        a. Add item
        b. Delete item
        c. Modify value
        """)

        sub_choice1 = input("Which subchoice would you like to select (r to return)? ").lower()
        
        if sub_choice1 == 'a':
            while True:
                add_where = input("Would you like to add to income (i) or expenses (e) (q to quit)? ").lower()
                if add_where == 'q':
                    print("Returning to main menu.")
                    break
                elif add_where == 'i':
                    add_to(inc_info)
                elif add_where == 'e':
                    add_to(exp_info)
                else:
                    print("Invalid input.")
                    continue
        elif sub_choice1 == 'b':
            while True:
                del_where = input("Would you like to delete from income (i) or expenses (e) (q to quit)? ").lower()
                if del_where == 'q':
                    print("Returning to main menu.")
                    break
                elif del_where == 'i':
                    del_from(inc_info)
                elif del_where == 'e':
                    del_from(exp_info)
                else:
                    print("Invalid input.")
                    continue
        elif sub_choice1 == 'c':
            while True:
                mod_where = input("Where would you like to modify a value, income (i) or expenses (e) (q to quit)? ").lower()
                if mod_where == 'q':
                    print("Returning to main menu.")
                    break
                elif mod_where == 'i':
                    mod_amount(inc_info)
                elif mod_where == 'e':
                    mod_amount(exp_info)
                else:
                    print("Invalid input.")
                    continue
        elif sub_choice1 == 'r':
            continue
        else:
            print("Invalid input.")
            continue
        

    elif choice == '2':
        print("""
        d. Recommended income
        e. Recommended expense
        f. Wants analysis
        """)

        sub_choice2 = input("Which subchoice would you like to select (r to return)? ").lower()

        if sub_choice2 == 'd':
            rec_inc()
        elif sub_choice2 == 'e':
            rec_exp()
        elif sub_choice2 == 'f':
            want_this()
        elif sub_choice2 == 'r':
            continue
        else:
            print("Invalid input.")
            continue
        

    elif choice == '3':
        print("""
        g. Play with current expenses
        h. Play with current income
        """)

        sub_choice3 = input("Which subchoice would you like to select (r to return)? ").lower()

        if sub_choice3 == 'g':
            budget_play(exp_info, 'exp')
        elif sub_choice3 == 'h':
            budget_play(inc_info, 'inc')
        elif sub_choice3 == 'r':
            continue
        else:
            print("Invalid input.")
            continue
        

    elif choice == '4':
        print("""
        i. View all budget information
        j. View all expense information
        k. View all income information
        l. View all information
        """)

        sub_choice4 = input("Which subchoice would you like to select (r to return)? ").lower()

        if sub_choice4 == 'i':
            view_dict(budget_plan, 'Budget Plan')
        elif sub_choice4 == 'j':
            view_dict(exp_info, 'Expenses')
        elif sub_choice4 == 'k':
            view_dict(inc_info, 'Income')
        elif sub_choice4 == 'l':
            view_dict(budget_plan, 'Budget Plan')
            view_dict(exp_info, 'Expenses')
            view_dict(inc_info, 'Income')
        elif sub_choice4 == 'r':
            continue
        else:
            print("Invalid input.")
            continue


    else:
        try_again = input("Invalid input. Would you like to try again? y/n: ")
        if try_again == "y":
            continue
        elif try_again == "n":
            print("Thank you for using our service. Come again!")
            exit()
        else:
            print("Invalid input.")
            continue
