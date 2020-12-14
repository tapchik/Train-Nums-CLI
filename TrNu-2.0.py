from random import randint
from random import choice
import json

#INITIALIZATION
data = {"addition": True,
        "subtraction": False,
        "max sum": 25,
        "problem": "0 + 0",
        "answer": 0,
        "correct": 0,
        "incorrect": 0,
        "skipped": 0}
solved = True
quitting = False

#SCRIPTS

def script_help():
    print('\n' + """You can enter listed commands when user input is prompted:

"skip" - skip difficult problems;
"settings" - change max sum;
"status" - show settings and your statistics;
"delete progress" - clear your statistics and start fresh;
"turn on/off addition";
"turn on/off subtraction";
"help" - show this list of commands again;
"exit" - quit Train Nums. """)

def script_settings():

    print('\n' + "Current max sum is: " + str(data["max sum"]))
    while True:
        try:
            x = int(input("Enter new max sum: "))
            return abs(x)
        except ValueError:
            print('\n' + "Number is required, try again... " + '\n')

def script_show_status():
    #displays settings and statistics

    print('\n' + "Max sum" + '     : ' + str(data["max sum"]))

    print("Addition", end='    : ')
    if data["addition"] == True:
        print("on")
    else:
        print("off")

    print("Subtraction", end=' : ')
    if data["subtraction"] == True:
        print("on")
    else:
        print("off")

    total = data["correct"] + data["incorrect"] + data["skipped"]

    print(' ')
    print("Correctly solved" + '      : ' + str(data["correct"]))
    print("Mistakes were made" + '    : ' + str(data["incorrect"]))
    print("Skipped problems" + '      : ' + str(data["skipped"]))
    print("Solved problems total" + ' : ' + str(total))

    try:
        print("{0}% of all problems are solved correctly".format(round(data["correct"]/total*100), 2))
    except ZeroDivisionError:
        print("Further statistics are not available")
        print('\n' + "Back to the problem... ")

#FUNCTIONS

def file_read():

    try:
        with open("TrNuSettings.json", "r") as file:
            data = json.load(file)
            if data["addition"] in [True, False] and data["subtraction"] in [True, False] and data["correct"] >= 0 and data["incorrect"] >= 0 and data["skipped"] >= 0 and data["max sum"] > 0:
                return data
            else:
                raise KeyError()

    except FileNotFoundError:
        print('\n' + "This is a first startup of Train Nums on this computer. ")
        print("We love seeing new users! ")
        return False

    except (KeyError, TypeError):
        print('\n' + "Settings file must be currupted. Did you try to cheat? ")
        print("Program is set to default settings and your progress was nullified. ")
        data = set_to_default()
        return False

def file_save():
    with open("TrNuSettings.json", "w") as file:
        json.dump(data, file, indent = 4)

def set_to_default():

    data = {"addition": True,
    	    "subtraction": False,
    	    "max sum": 25,
    	    "problem": "0 + 0",
    	    "answer": 0,
    	    "correct": 0,
    	    "incorrect": 0,
    	    "skipped": 0}
    return data

def choose_operation():

    options = []

    if data["addition"] == True:
        options.append("+")
    if data["subtraction"] == True:
        options.append("-")

    if options != []:
        return choice(options)
    return None

def generate_problem(operation):

    problem = str()

    #example
    # 123     '+'      456  =  579
    #left, operation, right, answer

    if operation == '+':

        answer = randint(1, data["max sum"])
        left = randint(1, answer)
        right = answer - left

        problem += str(left)
        problem += ' ' + operation + ' '
        problem += str(right)

    elif operation == '-':

        left = randint(1, data["max sum"])
        right = randint(1, left)
        answer = left - right

        problem += str(left)
        problem += ' ' + operation + ' '
        problem += str(right)

    elif operation == None:

        problem = None
        answer = None

    return (problem, answer)

#START OF PROGRAM

print('\n' + "Start of program... ")
data = file_read()
if data == False:
    solved = True
    data = set_to_default()
else:
    print("Reading from file... ")
    solved = False

script_help()

while True:

    if quitting == True:
        break

    if solved == True:
        operation = choose_operation()
        data["problem"], data["answer"] = generate_problem(operation)
        del operation
        solved = False

    if data["problem"] is not None:
        print('\n' + data["problem"])
    else:
        print('\n' + "Generation is turned off. Choose an operation. ")
        solved = True

    user = input("User input: ")

    if user.isdigit() == True:
        user = int(user)
    else:
        user = user.lower()

    if user == data["answer"]:
        print("Correct!")
        data["correct"] += 1
        solved = True

    elif isinstance(user, int):
        print('\n' + "Incorrect, try again")
        data["incorrect"] += 1

    elif user in ["exit", "quit"]:
        file_save()
        quitting = True

    elif user == "settings":
        data["max sum"] = script_settings()
        print("Back to math problem... ")

    elif user == "skip":
        print("We will count that. Next problem... ")
        data["skipped"] += 1
        solved = True

    elif user == "turn on addition":
        if data["addition"] == True:
            print('\n' + "Addition is already turned on")
        else:
            print('\n' + "Addition is turned on now")
            data["addition"] = True
        print("Back to math problem... ")

    elif user == "turn off addition":
        if data["addition"] == False:
            print('\n' + "Addition is already turned off")
        else:
            print('\n' + "Addition is turned off now")
            data["addition"] = False
        print("Back to math problem... ")

    elif user == "turn on subtraction":
        if data["subtraction"] == True:
            print('\n' + "Subtraction is already turned on")
        else:
            print('\n' + "Subtraction is turned on now")
            data["subtraction"] = True
        print("Back to math problem... ")

    elif user == "turn off subtraction":
        if data["subtraction"] == False:
            print('\n' + "Subtraction is already turned off")
        else:
            print('\n' + "Subtraction is turned off now")
            data["subtraction"] = False
        print("Back to math problem... ")

    elif user == "delete progress":
        data["correct"] = 0
        data["incorrect"] = 0
        data["skipped"] = 0
        print('\n' + "Your statistics were succesfully cleared... ")

    elif user == "status":
        script_show_status()
        print('\n' + "Back to the math problem... ")

    elif user == "help":
        print(' ')
        script_help()

    else:
        print('\n' + "Unknown command, try again... ")

input ('\n' + "End of program, press Enter to exit... ")
