# This is just me practicing to see that I still got it

def age_checker():
    try:
        birth_year = input("What is your year of birth?: ")
        if len(birth_year) != 4:
            print("Kindly enter birth year in this format 'yyyy'")
            age_checker()
        age = 2023 - int(birth_year)
        if age < 18:
            print("You are still a minor. You cannot be granted access")
        elif age < 21:
            print("Your age does not allow you to access all of the features")
        else:
            print("Access granted")
    except ValueError:
        print("You can only enter numbers. Try again")
        age_checker()


age_checker()



