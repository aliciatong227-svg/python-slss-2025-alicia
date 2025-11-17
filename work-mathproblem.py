# def age_add_thirtyone(age: int):
#     age += 31
#     return age

# def main():
#     print("How old are you now?")
#     age = int(input())
#     print(f"You will be {age_add_thirtyone(age)} in 2049!")


# if __name__ == "__main__":
#     main()


# def score_average(J1: float, J2: float, J3: float, J4: float, J5: float):
#     average = (J1 + J2 + J3 + J4 + J5) / 5
#     return average


# def main():
#     J1 = float(input("Judge 1:"))
#     J2 = float(input("Judge 2:"))
#     J3 = float(input("Judge 3:"))
#     J4 = float(input("Judge 4:"))
#     J5 = float(input("Judge 5:"))
#     print(f"Your olympic score is {score_average(J1, J2, J3, J4, J5)}")


# if __name__ == "__main__":
#     main()


def main():
    cost = float()
    print("Would you like a burger for $5? (Yea/No)")
    burger = input().lower().strip("?!,.")
    if burger == "yes":
        cost += 5
    else:
        cost += 0
    print("Would you like fries for $3? (Yea/No)")
    fries = input().lower().strip("?!,.")
    if fries == "yes":
        cost += 3
    else:
        cost += 0
    cost *= 1.14
    print(f"Your total is ${cost}.")


if __name__ == "__main__":
    main()
