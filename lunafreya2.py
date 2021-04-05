import json
import time
import enquiries
import pickle
import random

def load_info():
    with open('data.json') as user_info:
        user = json.load(user_info)
    return user

def check_user(username):
    for user in users:
        user_s = user["name"]
        if (username == user_s):
            print(username)

def save_file(user):
    f = open("data.json", "w")
    f = write(json.dumps(user, indent = 2))
    f.close()
   

user = load_info()

print("Hi! I am Luna, your personal health assistant")

time.sleep(2)

#print("Please, show me who you are!")
    
# def login(usr):
#    user["usrname"] = input("Name: ")
#    user["pssword"] = input("Password: ")

#    if uN in usr.keys():
#        if user["pssword"] == usr(user["usrname"]):
#            print("Welcome back.")
#        else:
#            print("Incorrect password.")
#            return False
#    else:
#        print("Hello, new person.")
#    writeUsers(usr)
#    return True

#def readUsers():
#    try:
#        with open("data.json", "r") as f:
#            return json.load(f)
#    except FileNotFoundError:
#        return {}

#def writeUsers(usr):
#    with open("data.json", "w+") as f:
#            json.dump(usr, f, indent = 2)

#users = readUsers()
#success = login(users)

#while not success:
#    success = login(users)

print("Please help me to understand what is your case so I can help you!")

time.sleep(2)

user["name"] = input("First of all, what is your name? ")

print("Oh hi,", user["name"], ", you look gorgeous today!")

time.sleep(2)

print("Okay, now give me some more info")

time.sleep(2)

user["assumed_gender"] = ["Male", "Female"]

choice = enquiries.choose("Your Assumed Gender: ", user["assumed_gender"])

print(choice)

user["weight"] = float(input("I know this one is a personal one but... How much do you weight? (in kg's, please... I am Europian) "))

time.sleep(2)

user["height"] = float(input("How tall are you (in cm, please...) "))

time.sleep(2)

print("I know we live in an environment where you don't even have to walk as anything can be done online, but...")

user["activity_level"] = ["Low", "Medium", "High"]

choice =  enquiries.choose("What is your daily level of activity? This means walking, jogging, other sports (walking to get your TV remote is an activity too): ", user["activity_level"])

print(choice)

print("Okay, now calculating some stuff... (*beep bop beep* and other cliche robot noises...)")

time.sleep(3)

bmi = round(user["weight"] / (user["height"]/100)**2)

print("Your body mass index is", bmi, ", which is...")

if (bmi<18.5):
    print("Very bad. You are extremaly underweight and you need to see your doctor to try and fix it, I cannot help in this case. Please, go to your doctor as soon as possible and stay healthy.")

if (18.5<bmi<24.9):
    
    print("Average. You are in a pretty good shape and I can give some advices on how to keep that shape!")
    
    average = ["Diet Advices", "Exercises", "Good Habits", "Bad Habits Monitor"]
    
    choice = enquiries.choose("On which of these you want an advice?", average)
    
    print(choice)

    if (choice == "Exercises"):
        

        average_exercise = ["a", "b", "c", "d"]
        
        rand_av_ex = random.choice(average_exercise)
        
        print(rand_av_ex)


    
    elif (choice == "Diet Advices"):
        
        average_diet = ["a", "b", "c", "d"]
    
        rand_av_diet = random.choice(average_diet)

        print(rand_av_diet)
    
    
    elif (choice == "Good Habits"):

        average_habits = ["a", "b", "c", "d"]

        rand_av_hab = random.choice(average_habits)

        print(rand_av_hab)

    
    elif (choice == "Bad Habits Monitor"):

        b_habits = ["Smoking", "Alcohol Usage"]

        choice = enquiries.choose("What bad habits do you have?", b_habits)

        print(choice)



if (25<bmi<29.9):
    
    print("Above Average. You are overweight but it can be fixed with the help of regular exercises and healthy eating habits, and I can surely help with that!")

if (30<bmi):
    
    print("Very bad. This weight can be catastrophic for your organism, you need to see your doctor as soon as you can! I cannot help with this situation, only professional can. See a doctor as soon as possible and stay healthy.")
