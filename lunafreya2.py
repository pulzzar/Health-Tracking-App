import json
import time
import enquiries
import pickle
import random
import sys
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


overweight_list = ["- High blood pressure", "- Type II diabetes", "- Coronary heart disease", "- Stroke", "- Gallbladder disease", "- Sleep apnea and breathing problems", "- Certain cancers (endometrial, breast, colon, kidney, gallbladder, liver)", "- Low quality of life", "- Mental illnesses such as clinical depression, anxiety, and others", "- Body pains and difficulty with certain physical functions"]

underweight_list = ["- Malnutrition, vitamin deficiencies, anemia (lowered ability to carry blood vessels)",
"- Osteoporosis, a disease that causes bone weakness, increasing the risk of breaking a bone", "- A decrease in immune function"
"- Growth and development issues, particularly in children and teenagers"]

advice_overweight = ["- Diet. A steady weight loss of about one pound a week is the safest way to lose weight.",
"- Regular exercise such as brisk walking, running, swimming, biking, dancing. The amount of exercise needed to lose weight is different for everyone.",
"Behavior modification techniques such as:",
"",
"- Keep a food diary of everything you eat.",
"- Shop from a list and do not shop when you're hungry.",
"- Take a different route if you usually pass by a tempting fast food place.",
"",
"If you have been unable to lose weight or keep if off with diet, exercise, and behavior changes:",
"",
"- Weight-loss medications might be recommended for you.",
"- Gastrointestinal surgery is sometimes recommended for people with severe obesity."]
diet_obesity = ["First option.", "", "Does not contain any animal product (meat, fish, poultry, eggs, or dairy) but emphasizes plant-based foods, such as fruits, vegetables, whole grains, and legumes/beans", "", "Second option.", "", "Does not contain meat, fish, or poultry but does contain eggs and dairy, in addition to plant-based foods, such as fruits, vegetables, whole grains, and legumes/beans", "", "Salad - Black-eyed peas and brown rice with chopped tomatoes and roasted peppers."]

diet_overweight = ["First option.", "", "Contains all foods, including meat, poultry, fish and shellfish, eggs and dairy, in addition to plant-based foods, such as fruits, vegetables, whole grains, and legumes/beans. However, red meat and poultry and fairly limited",
"Second option.", "",  "Contains all food groups",
"Salad - Black-eyed peas and brown rice with low-fat sausage, chopped tomatoes, roasted peppers, and reduced fat cheddar cheese"]

vegan_meals = ["Avocado.",
"Quinoa.",
"Tahini." ,
"Olive Oil.",
"Dried Fruit.",
"Legumes.",
"Sweet Potatoes."]

non_vegan_meals = ["Meat (beef, pork, lamb, and other red meats)",
"Eggs" ,
"Cheese",
"Butter",
"Dairy products",
"Snacks that contain plenty of protein and healthy carbohydrates (jerky, trail mix, Greek yogurt parfait…)",
"Potatoes and starches.",
"Salmon and oily fish.",
"Nuts and nut butters.",
"Protein shakes. Protein shakes can help a person to gain weight easily and efficiently."
]


print("Hi! I am Luna, your personal health assistant")

for char in "Hi! I am Luna, your personal health assistant":
    print(char, end="")
    sys.stdout.flush()
    time.sleep(0.2)

time.sleep(2)

print("Please, show me who you are!")
    
def login(usr):
    user["usrname"] = input("Name: ")
    user["pssword"] = input("Password: ")

    if uN in usr.keys():
        if user["pssword"] == usr(user["usrname"]):
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return False
    else:
        print("Hello, new person.")
    writeUsers(usr)
    return True

def readUsers():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("data.json", "w+") as f:
            json.dump(usr, f, indent = 2)

users = readUsers()
success = login(users)

while not success:
    success = login(users)

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
    
    print("Very bad. You are extremaly underweight and you need to see your doctor to try and fix it.")
    
    print("Being underweight has its own associated risks, listed below")
    
    for item2 in underweight_list:
        
        print(item2)

    under = ["Diet Advices", "Exercises"]

    choice = enquiries.choose("On which of these you want an advice?", under)

    print(choice)

    if (choice == "Exercises"):

        print("Your BMI is", bmi, "so here are some exercises for you")

        if (bmi<16):

            exsixteen = ["10 push ups","10 press","20 jumping jacks", "10 sit ups","20s plank + 5k Jog"]
            
            for item in exsixteen:

                print(item)

                sys.stdout.flush()

                time.sleep(1)

        if (bmi<17):

            seventeen = ["15 push ups","15 press","25 jumping jacks","15 sit ups","25s plank + 5k Jog"]

            for item in seventeen:

                print(item)

                sys.stdout.flush()

                time.sleep(1)

    if (choice == "Diet Advices"):
        
        vegnonveg = ["Vegan Meals", "Non-vegan Meals"]

        choice = enquiries.choose("Are you a vegan or a non-vegan?", vegnonveg)

        print(choice)

        print("Okay, so you chose", choice, "then here are some advices and meals you SHOULD eat")

        if (choice == "Vegan Meals"):
            
            for veg in vegan_meals:

                print(veg)

                sys.stdout.flush( )

                time.sleep(1)

        if (choice == "Non-vegan Meals"):

            for non_veg in non_vegan_meals:

                print(non_veg)

                sys.stdout.flush()

                time.sleep(1)



if (18.5<bmi<24.9):
    
    print("Average. You are in a pretty good shape and I can give some advices on how to keep that shape!")
    
    average = ["Diet Advices", "Exercises", "Good Habits", "Bad Habits Monitor"]
    
    choice = enquiries.choose("On which of these you want an advice?", average)
    
    print(choice)

    if (choice == "Exercises"):
        
    

        if (bmi>18.5):
            
            print("Your BMI is", bmi, "So here are some exercises for you")

            average_exercise = ["20 push ups","20 press","30 jumping jacks","20 sit ups","30s plank + 5k Jog"]
        
            for item in average_exercise:
            
                print(item)

                sys.stdout.flush()

                time.sleep(1)
                

    
    elif (choice == "Diet Advices"):
        
        average_diet = ["a", "b", "c", "d"]
    
        rand_av_diet = random.choice(average_diet)

        print(rand_av_diet)
    
    
    elif (choice == "Good Habits"):

        average_habits = ["a", "b", "c", "d"]

        rand_av_hab = random.choice(average_habits)

        print(rand_av_hab)



if (25<bmi<29.9):
    
    print("Above Average. You are overweight but it can be fixed with the help of regular exercises and healthy eating habits, and I can surely help with that!")
    
    print("Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks.")
    
    for item in overweight_list:
        
        print(item)

    lower_overweight = ["Diet Advices"]

    choice = enquiries.choose("Advice:", lower_overweight)

    print(choice)

    if (choice == "Diet Advices"):

        print("There are two options for you right now")
        
        for diet in diet_overweight:

            print(diet)

            sys.stdout.flush()

            time.sleep(.2)

if (30<bmi):
    
    print("Very bad. This weight can be catastrophic for your organism, you need to see your doctor as soon as you can!")

    print("Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks.")

    for item in overweight_list:

        print(item)

        sys.stdout.flush()
        
        time.sleep(1)
    
    print("So what advices can I give?")

    for advice in advice_overweight:
        
        print(advice)
        
        sys.stdout.flush()

        time.sleep(1)



    overweight = ["Diet Advices"]

    choice = enquiries.choose("Advice:", overweight)

    print(choice)

    if (choice == "Diet Advices"):

        print("There are two options for you right now")
        
        for item in diet_obesity:
            
            print(item)

            sys.stdout.flush()

            time.sleep(1)

    
