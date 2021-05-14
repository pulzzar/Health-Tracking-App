import json
import time
import enquiries
import pickle
import sys

def load_info():
    with open('data.json') as user_info:
        user = json.load(user_info)
    return user

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

print("Hi! I am Luna, your personal health assistant")

print("Please help me to understand what is your case so I can help you!")

time.sleep(1) 

user["name"] = input("First of all, what is your name? ")

print("Oh hi,", user["name"], ", you look gorgeous today!")

time.sleep(1)

print("Okay, now give me some more info")

time.sleep(1)

user["assumed_gender"] = ["Male", "Female"]

choice = enquiries.choose("Your Assumed Gender: ", user["assumed_gender"])

print(choice)

user["weight"] = float(input("I know this one is a personal one but... How much do you weight? (in kg's, please... I am Europian) "))

time.sleep(1)

user["height"] = float(input("How tall are you (in cm, please...) "))

print("Okay, now calculating some stuff... (*beep bop beep* and other cliche robot noises...)")

time.sleep(2)

bmi = round(user["weight"] / (user["height"]/100)**2)

print("Your body mass index is", bmi, ", which is...")


if (bmi<18.5):
    
    print("Very bad. You are extremaly underweight and you need to see your doctor to try and fix it.")
    
    print("Being underweight has its own associated risks, listed below")
    
    for item2 in underweight_list:
        
        print(item2)

    
    def menu():
    
        print("Press The Key To Choose\n  1. Diet \n 2. Exercises \n 3. Exit")

        option = input()

        if (option == "2"):

            print("Your BMI is", bmi, "so here are some exercises for you")

            user["exercise"]["jog"] = "5km"

            user["exercise"]["plank"] = "25s"
                
            user["exercise"]["pushup"] = 15

            user["exercise"]["press"] = 15

            user["exercise"]["squat"] = 15

            user["exercise"]["jumping_jack"] = 25
                
            print("Jogging: ", user["exercise"]["jog"], "Plank: ", user["exercise"]["plank"], "Push-up: ", user["exercise"]["pushup"],"Press: ", user["exercise"]["press"], "Squats: ", user["exercise"]["squat"], "Jumping Jacks: ", user["exercise"]["jumping_jack"], sep='\n')
            
            menu()
        
            
        if (option == "1"):
            
            vegnonveg = ["Vegan Meals", "Non-vegan Meals"]

            choice = enquiries.choose("Are you a vegan or a non-vegan?", vegnonveg)

            print(choice)

            print("Okay, so you chose", choice, "then here are some advices and meals you SHOULD eat")

            if (choice == "Vegan Meals"):
                
                user["meals"]["1"] = "Avocado"
                
                user["meals"]["2"] = "Quinoa"
                
                user["meals"]["3"] = "Tahini"
                
                user["meals"]["4"] = "Olive Oil"
                
                user["meals"]["5"] = "Dried Fruits"
                
                user["meals"]["6"] = "Legumes"
                
                user["meals"]["7"] = "Sweet Potatoes"
                
                print(user["meals"]["1"], user["meals"]["2"],user["meals"]["3"],user["meals"]["4"],user["meals"]["5"],user["meals"]["6"],user["meals"]["7"], sep = '\n')

                menu()

            if (choice == "Non-vegan Meals"):

                user["meals"]["1"] = "Meat (beef, pork, lamb, and other red meats)"
                
                user["meals"]["2"] = "Eggs"
                
                user["meals"]["3"] = "Cheese"
                
                user["meals"]["4"] = "Butter"
                
                user["meals"]["5"] = "Dairy products"
                
                user["meals"]["6"] = "Snacks that contain plenty of protein and healthy carbohydrates"
                
                user["meals"]["7"] = "Potatoes and starches."
                
                user["meals"]["8"] = "Salmon and oily fish."
                
                user["meals"]["9"] = "Nuts and nut butters."
                
                user["meals"]["10"] = "Protein shakes. Protein shakes can help a person to gain weight easily and efficiently."
                
                print(user["meals"]["1"], user["meals"]["2"],user["meals"]["3"],user["meals"]["4"],user["meals"]["5"],user["meals"]["6"],user["meals"]["7"],user["meals"]["8"],user["meals"]["9"],user["meals"]["10"], sep = '\n')
                
                menu()
    menu()

if (18.5<bmi<24.9):
    
    print("Average. You are in a pretty good shape and I can give some advices on how to keep that shape!")

    #average = ["Diet Advices", "Exercises"]
    
    #choice = enquiries.choose("On which of these you want an advice?", average)
    
    def menu():

        print("Press The Key To Choose\n  1. Exercises \n 2. Exit")

        option = input()


        if (option == "1"):
            
            user["exercise"]["jog"] = "5km"

            user["exercise"]["plank"] = "30s"

            user["exercise"]["pushup"] = 20

            user["exercise"]["press"] = 20

            user["exercise"]["squat"] = 20

            user["exercise"]["jumping_jack"] = 30 

            print("Jogging: ", user["exercise"]["jog"], "Plank: ", user["exercise"]["plank"], "Push-up: ", user["exercise"]["pushup"],"Press: ", user["exercise"]["press"], "Squats: ", user["exercise"]["squat"], "Jumping Jacks: ", user["exercise"]["jumping_jack"], sep='\n')
            menu()
            
        if (option == "2"):
            
            quit()

    menu()

if (25<bmi<29.9):
    
    print("Above Average. You are overweight but it can be fixed with the help of regular exercises and healthy eating habits, and I can surely help with that!")
    
    print("Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks.")
    
    for item in overweight_list:
        
        print(item)

    def menu():

        print("Press The Key To Choose\n  1. Diet \n 2. Exit")

        option = input()
        
        def submenu():

            print("Press The Key To Choose\n  a. Option 1 \n s. Option 2 \n d. Go back")

            option = input()

            if (option == "a"):

                print("There are two options for you right now")

                user["meals"]["1"] = "First: "

                user["meals"]["2"] = "No animal products (except of fish and eggs)"

                user["meals"]["3"] = "Lot of plant based foods"

                user["meals"]["4"] = "Fruits"

                user["meals"]["5"] = "Vegetables"

                user["meals"]["6"] = "Legumes/beans"

                user["meals"]["7"] = "Whole Grains"

                user["meals"]["8"] = "Salad option: Black-eyed peas and brown rice with chopped tomatoes and roasted peppers"

                print(user["meals"]["1"], user["meals"]["2"],user["meals"]["3"],user["meals"]["4"],user["meals"]["5"],user["meals"]["6"],user["meals"]["7"], user["meals"]["8"], sep = '\n')

                submenu()

            elif (option == "s"):

                user["meals"]["1"] = "Second: "

                user["meals"]["2"] = "No animal products (except of eggs, dairy, fish and shellfish)"

                user["meals"]["3"] = "Lot of plant based foods"

                user["meals"]["4"] = "Fruits"

                user["meals"]["5"] = "Vegetables"

                user["meals"]["6"] = "Legumes/beans"

                user["meals"]["7"] = "Whole Grains"

                user["meals"]["8"] = "Black-eyed peas and brown rice with shrimp, chopped tomatoes, roasted peppers and reduced fat cheddar cheese"

                print(user["meals"]["1"], user["meals"]["2"],user["meals"]["3"],user["meals"]["4"],user["meals"]["5"],user["meals"]["6"],user["meals"]["7"], user["meals"]["8"], sep = '\n')

                submenu()

            elif (option == d):
                
                menu()

        submenu()
    
    menu()

            

if (30<bmi):
    
    print("Very bad. This weight can be catastrophic for your organism, you need to see your doctor as soon as you can!")

    print("Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks.")

    for item in overweight_list:

        print(item)

        sys.stdout.flush()
        
        time.sleep(1)

    def menu():

        print("Press The Key To Choose\n  1. Diet \n 2. Exit")

        option = input()

        def submenu():

            print("Press The Key To Choose\n  a. Option 1 \n s. Option 2 \n d. Go back")

            option = input()
    
            if (option == "a"):

                print("There are two options for you right now")

                user["meals"]["1"] = "First: "
                
                user["meals"]["2"] = "No animal products (except of fish and eggs)"
                
                user["meals"]["3"] = "Lot of plant based foods"
                
                user["meals"]["4"] = "Fruits"
                
                user["meals"]["5"] = "Vegetables"
                
                user["meals"]["6"] = "Legumes/beans"
                
                user["meals"]["7"] = "Whole Grains"

                user["meals"]["8"] = "Salad option: Black-eyed peas and brown rice with chopped tomatoes and roasted peppers"
                
                print(user["meals"]["1"], user["meals"]["2"],user["meals"]["3"],user["meals"]["4"],user["meals"]["5"],user["meals"]["6"],user["meals"]["7"], user["meals"]["8"], sep = '\n')
                
                submenu()

            elif (option == "s"):
                
                user["meals"]["1"] = "Second: "

                user["meals"]["2"] = "No animal products including fish our poultry (except of eggs and dairy"

                user["meals"]["3"] = "Lot of plant based foods"

                user["meals"]["4"] = "Fruits"

                user["meals"]["5"] = "Vegetables"

                user["meals"]["6"] = "Legumes/beans"

                user["meals"]["7"] = "Whole Grains"

                user["meals"]["8"] = "Salad option: Black-eyed peas and brown rice with chopped tomatoes and roasted peppers"
                
                print(user["meals"]["1"], user["meals"]["2"],user["meals"]["3"],user["meals"]["4"],user["meals"]["5"],user["meals"]["6"],user["meals"]["7"], user["meals"]["8"], sep = '\n')
                
                submenu()

            elif (option == "d"):

                menu()
            
        if (option == "3"):
            
                quit()
        
        submenu()
    
    menu()
