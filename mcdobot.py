# Write a McDonald's bot that asks if you want fries with your meal.
# Call it work-mcdobot.py.
# It should accept Yes/yes or No/no as inputs, and replyappropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.

help = (
    input("Welcome to Mcdonald, is there anything you want?(yes or no)")
    .lower()
    .strip(".,?!")
)

if help == "no":
    print("Ok, see you next time")
elif help == "yes":
    print("Sounds good! what food would you like.")
    food = input().lower().strip("?!.,")
    fries = (
        input(f"Ok, so you want {food}, would you like to have fries with your meal?")
        .lower()
        .strip("?!.,")
    )
    drink = input("Ok, do you also want drink for your meal?").lower().strip("?!.,")
    if fries == "yes" and drink == "yes":
        print("Here is your meal with fries and drink!")
    elif fries == "yes" and drink == "no":
        print("Here is your meal with fries only!")
    elif fries == "no" and drink == "yes":
        print("Here is your meal with drink only!")
    elif fries == "no" and drink == "no":
        print("Here is your meal!")
    else:
        print(f"Sorry, I don't understand what is {fries} and {drink}!")
else:
    print(f"Sorry, I don't understand what is {help}")
