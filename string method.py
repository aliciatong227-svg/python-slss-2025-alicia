# Ask the user what ther weather is like
weather = input("What is the waether is like?").lower().strip("?!.,")
if weather == "rainy":
    print("You should bring an umbrella")
elif weather == "sunny":
    print("You should ut on your eye glasses")
else:
    print("I see...")

# ask the customer if they want fries
fries_reply = input("Do you want fries")  # "yes!"

if "yes" in fries_reply:
    print("Here are your fries.")
else:
    print("OK, You will not have fries.")
