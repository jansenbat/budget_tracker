"""
Why: keep track of my expenses, savings, and wants
    - Used to see if I can afford things or not
    - Used to help plan bills payments better
    - Used to control my spending because honestly sometimes I have no idea what my financial ability is
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

inc_fix = {}
inc_var = {}
inc_total = []   # make equation that takes the total of all incomes

exp_fix = {}
exp_var = {}
exp_total = []   # make equation that takes the total of all incomes

budget_plan = {
    'expenses' : 50,
    'wants' : 30,
    'savings' : 20
}

def add_to(aDict, name_of):   # function that adds new entries to a dictionary
    """
    aDict: any dictionary to add to
    name_of: a string, just used to print the name of the dictionary being interacted with
    """
    add_name = input("What is the name of the " + name_of + ": ")
    add_amount = input("What is the amount of the " + name_of + ": ")
    aDict[add_name.lower()] = float(add_amount)

def del_from(aDict, name_of):   # function that deletes a key-value pair from a dictionary
    """
    aDict: any dictionary to delete from
    name_of: a string, just used to print the name of the dictionary being interacted with
    """
    while True:
        print(aDict)
        print("To quit this action, enter 'q'.")
        del_name = input("Which " + name_of + " would you like to delete? Enter name: ").lower()
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
            del_more = input("Would you like to delete another " + name_of +"? y/n: ")
            if del_more == 'y':
                continue
            elif del_more == 'n':
                break
            else:
                print("Invalid input.")
                continue   # send the user back to the top of the while loop
        else:
            ask_again = input("We don't see that " + name_of + ". Would you like to try again? ").lower()
            if ask_again == 'y':
                continue
            elif ask_again == 'n':
                break
            else:
                print("Invalid input.")
                continue   # send the user back to the top of the while loop

def view_dict(aDict, name_of):   # function that allows the user to view their dictionary
    """
    aDict: any dictionary the user would like to view
    name_of: just used to display the name of the dictionary being accessed
    """
    print("Currently Viewing: " + name_of)
    for key, value in aDict.items():
        print(key + " : " + str(value))

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

def rec_exp(d1, d2):
    d1_values = d1.values()
    d1_total = sum(d1_values)
    d2_values = d2.values()
    d2_total = sum(d2_values)
    recommended_ratio = int((d1_total / d2_total) * 100)
    print("Based on your financial standing, the recommended expense allocation ratio is: " + str(recommended_ratio) + ".")


def purchase_adv():
    pass

def expense_adv():
    pass

def ideal_inc():
    pass

def ideal_exp():
    pass

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
            a. Modify income (fixed and variable)
            b. Modify expenses (fixed and variable)
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

