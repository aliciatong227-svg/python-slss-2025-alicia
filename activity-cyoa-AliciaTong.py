# Choose Your Own Adventure
# Author: Alicia Tong
# 24 September 2025

# Choose your own adventure story focusing on using variables and branching/conditions.

import time
import os
import random


# Intro
print("Hello everyone! Welcome to Time Travel 1.0!")
time.sleep(1.0)
name1 = input("Before we start, please enter you name.").strip("!?,.")
print(f"Welcome {name1}!")
time.sleep(1.0)
print("Now, lets get started!")
time.sleep(2.0)
os.system("clear")


# Rising
print(
    "You are chatting with your bestie, Alex, and you learn that he just invented a new time travel machine...\n"
)
time.sleep(2.0)
print(f"{name1}: Hi Alex, long time no see, what are you working on now?")
time.sleep(2.0)
print(
    "Alex: Oh hi! I just invented a time travelling machiene! I am pretty pround of myself!"
)
time.sleep(2.0)
print(f"{name1}: Wow, that is impressive!!")
time.sleep(1.0)
print("Alex: YESS! Do you want to come try out this lovely machiene?")
time.sleep(2.0)
ans1 = (
    input("Please type you answer here, if yes type yes, if no type no")
    .strip("?!,.")
    .lower()
)
os.system("clear")


def goHome():
    print("You decided to go home...delivered back!")
    time.sleep(2.0)
    choice = input("Do you want to go other place?").lower().strip("?!.,")
    if choice == "yes":
        choiceOfDestination()
    else:
        print(f"You have finish your adventure, hope to meet you again.{name1}")


def stay():
    stay = input("Do you want to stay? Yes/No")
    if stay == "no":
        goHome()
    else:
        print("Please wait for update...")
        choice = input("Do you want to go other place?").lower().strip("?!.,")
        if choice == "yes":
            choiceOfDestination()
        else:
            print("You decided to go home...delivered back!")
            print("Bye")


def choiceOfDestination():
    print("Alex: Thats perfect, Come here amd lemme show you!!")
    time.sleep(2.0)
    print("Here, you can choose where to go and now all the choice is...")
    time.sleep(1.0)
    print(" a)ancient_China\n b)future")
    ans2 = input("Please Choose you destination, a/b")
    if ans2 == "a":
        ancient_China()
    elif ans2 == "b":
        future()


def ancient_China():
    print("Welcome to ancient china")
    time.sleep(2.0)
    print("Alex: Wow, looks like we come to the Tang Denasty!")
    time.sleep(2.0)
    print(
        f"{name1}: Wow, this is actualy impressive! By the way, Let's get a change of clothes...We look weird"
    )
    time.sleep(2.0)
    print(
        "You guys walk across the streeet to get some clothings, but looks like you face some problem..."
    )
    time.sleep(1.0)
    print("Alex: Umm, I think I forgot to get the Tang money😅")
    ans3 = (
        input(
            "You only got enough money to buy one set, would you:\na) ask someone on the road\nb) go back to the machiene to get some"
        )
        .lower()
        .strip("?!,.")
    )
    if ans3 == "a":
        meetMeiLing()
    elif ans3 == "b":
        buyClothes()


def buyClothes():
    print(
        "You guys went back to the machiene to get some money, then you guys meet a lot of fun things."
    )
    time.sleep(2.0)
    tired = input(
        "After a whole day, you are kind of tired and out of money, do you want to\na) go home\nb) Keep wandering"
    )
    if tired == "a":
        print(
            "You and Alex decided to go back to the hotel to get some sleep, the other day..."
        )
        time.sleep(2.0)
        goBack()

    elif tired == "b":
        meetMeiLing()


def goBack():
    print("You found that you are back to the time travel machiene")
    time.sleep(2.0)
    print("What is happening? Why am I back here?")
    time.sleep(2.0)
    print("Machiene: Sorry, you fail your mission, please choose your destination.")
    time.sleep(2.0)
    print("HUH?")
    choiceOfDestination()


def meetMeiLing():
    print("Alex: Hi there! I'm sorry, can you lend me some money?")
    time.sleep(2.0)
    print("???: NiHao?")
    time.sleep(2.0)
    language = (
        input(
            "Looks like there is a problem for you guys to understand what they are saying, do you want translation?\nyes or no"
        )
        .strip("?!.,")
        .lower()
    )
    if language == "yes":
        meetMeiLing_english()
    elif language == "no":
        meetMeiLing_chinese()


choice = [goHome(), goBack()]


def meetMeiLing_chinese():
    print("MeiLing: Dui Bu Qi, Ni Shi Chuang Yue De Ma?")
    time.sleep(2.0)
    print(f"{name1}: Yes, we are, how do you know?!")
    time.sleep(2.0)
    print("MeiLing: Na Jiu Hao Le! Wo Men xu Yao Ni He Wo Men Jiu Bi Xia, Qing Lai Ba!")
    time.sleep(2.0)
    ans3 = input("Are you going? Yes/No").strip("?!'.").lower()
    if ans3 == "yes":
        goSaveTheKing()
    elif ans3 == "no":
        random.choice(choice)


def meetMeiLing_english():
    print("MeiLing: Sorry, can you say... Are you a time traveller?")
    time.sleep(2.0)
    print(f"{name1}: Yes, we are, how do you know?!")
    time.sleep(2.0)
    print(
        "MeiLing: That's perfect! We've found you for so longgg! I'm MeiLing, please come with me to save the king!"
    )
    time.sleep(2.0)
    ans3 = input("Are you going? Yes/No").strip("?!'.").lower()
    if ans3 == "yes":
        goSaveTheKing()
    elif ans3 == "no":
        random.choice(choice)


def goSaveTheKing():
    print(
        "Then you learnt that you are now just days before an assassination against King Xuanzong would plunge the empire into chaos. \nTeaming up with MeiLing's family, you secretly warned the King’s trusted general through a coded message. During the royal procession, you thwarted the assassins and safely evacuated the emperor through a hidden gate. \nThe rebellion was delayed, allowing the Tang Dynasty a longer era of peace, though new political rivalries emerged..."
    )
    time.sleep(5.0)
    stay()


def future():
    print("welcome to the 2100")


counter = 0
while counter != 100:
    if ans1 == "yes":
        choiceOfDestination()
        break
    elif ans1 == "no":
        goHome()
        break
    else:
        counter += 1
        ans1 = (
            input("Please type you answer here, if yes type yes, if no type no")
            .strip("?!,.")
            .lower()
        )
