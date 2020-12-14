from random import randint
from random import choice
import json

#INITIALIZATION
data = {"addition": True,
        "subtraction": False,
        "multiplication": True,
        "division": False,
        "max sum": 25,
        "max factor": 10,
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
"settings" - change max sum and max factor;
"status" - show settings and your statistics;
"delete progress" - clear your statistics and start fresh;
"operations" - which math operations to enable;
"help" - show this list of commands again;
"exit" - quit Train Nums. """)

def script_settings():

    global data

    print('\n' + "Current max sum is: " + str(data['max sum']))
    while True:
        try:
            user = int(input("Enter new max sum: "))
            data['max sum'] = user
            break
        except ValueError:
            print('\n' + "Number is required, try again... " + '\n')

    print('\n' + "Current max factor is: " + str(data['max factor']))
    while True:
        try:
            user = int(input("Enter new max factor: "))
            data['max factor'] = user
            break
        except ValueError:
            print('\n' + "Number is required, try again... " + '\n')

def script_operation():

    global data
    print('\n' + "Enter operations you want to enable, choose from +, -, * and /")

    while True:

        user = input("Enter operations: ")

        if '+' in user:
            data['addition'] = True
        else:
            data['addition'] = False

        if '-' in user:
            data['subtraction'] = True
        else:
            data['subtraction'] = False

        if '*' in user:
            data['multiplication'] = True
        else:
            data['multiplication'] = False

        if '/' in user:
            data['division'] = True
        else:
            data['division'] = False

        if '+' not in user and '-' not in user and '*' not in user and '/' not in user:
            print('\n' + "You should have at least one operation enabled")
        else:
            break

def script_show_status():
    #displays settings and statistics

    print('\n' + "Max sum    : " + str(data['max sum']))
    print("Max factor : " + str(data['max factor']))

    print(' ')
    print("Addition (+)", end='       : ')
    if data["addition"] == True:
        print("on")
    else:
        print("off")

    print("Subtraction (-)", end='    : ')
    if data["subtraction"] == True:
        print("on")
    else:
        print("off")

    print("Multiplication (*)", end=' : ')
    if data['multiplication'] == True:
        print("on")
    else:
        print("off")
    print("Division (/)", end='       : ')
    if data['division'] == True:
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

    global data
    
    try:
        with open("TrNuSettings.json", "r") as file:
            data = json.load(file)
            # TO-DO: check for mult and div
            if data["addition"] in [True, False] and data["subtraction"] in [True, False] and data["correct"] >= 0 and data["incorrect"] >= 0 and data["skipped"] >= 0 and data["max sum"] > 0:
                return True
            else:
                raise KeyError()

    except FileNotFoundError:
        print('\n' + "This is a first startup of Train Nums on this computer. ")
        print("We love seeing new users! ")
        return False

    except TypeError:
        print('\n' + "Settings file must be currupted. Did you try to cheat? ")
        print("Program is set to default settings and your progress was nullified. ")
        set_to_default()
        return False
    try:
        data["multiplication"]
        data["division"]
        data["max factor"]
    except KeyError:
        data["multiplication"] = False
        data["division"] = False
        data["max factor"] = 10
    return data

def file_save():
    with open("TrNuSettings.json", "w") as file:
        json.dump(data, file, indent = 4)

def set_to_default():
    global data
    data = {"addition": True,
    	    "subtraction": False,
            "multiplication": True,
            "division": False,
    	    "max sum": 25,
            "max factor": 10,
    	    "problem": "0 + 0",
    	    "answer": 0,
    	    "correct": 0,
    	    "incorrect": 0,
    	    "skipped": 0}

def choose_operation():

    options = []

    if data["addition"] == True:
        options.append("+")
    if data["subtraction"] == True:
        options.append("-")
    if data["multiplication"] == True:
        options.append("*")
    if data["division"] == True:
        options.append("/")

    if options != []:
        return choice(options)
    return None

def generate_problem(operation):

    problem = str()

    #example
    # 123     '+'      456  =  579
    #left, operation, right, answer

    if operation == None:
        problem = None
        answer = None
        return (problem, answer)

    elif operation == '+':
        answer = randint(1, data['max sum'])
        left = randint(1, answer)
        right = answer - left

    elif operation == '-':
        left = randint(1, data['max sum'])
        right = randint(1, left)
        answer = left - right

    elif operation == '*':
        left = randint(1, data['max factor'])
        right = randint(1, data['max factor'])
        answer = left * right

    elif operation == '/':
        right = randint(1, data['max factor'])
        answer = randint(1, data['max factor'])
        left = answer * right

    problem += str(left)
    problem += ' ' + operation + ' '
    problem += str(right)

    return (problem, answer)

#START OF PROGRAM

print('\n' + "Start of program... ")
if file_read() == True:
    print("Reading from file... ")
    solved = False
else:
    set_to_default()
    solved = True

script_help()

while True:

    if quitting == True:
        break

    if solved == True:
        operation = choose_operation()
        data["problem"], data["answer"] = generate_problem(operation)
        solved = False

    if data["problem"] is not None:
        print('\n' + data["problem"])
    else:
        print('\n' + "Generation is turned off. Choose operations. ")
        script_operation()
        solved = True
        continue

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
        script_settings()
        print('\n' + "Back to math problem... ")

    elif user == "skip":
        print("We will count that. Next problem... ")
        data["skipped"] += 1
        solved = True

    elif user == "operations":
        script_operation()
        print('\n' + "Back to math problem... ")

    elif user == "delete progress":
        data["correct"] = 0
        data["incorrect"] = 0
        data["skipped"] = 0
        print('\n' + "Your statistics were succesfully cleared... ")

    elif user == "status":
        script_show_status()
        print('\n' + "Back to math problem... ")

    elif user == "help":
        script_help()

    else:
        print('\n' + "Unknown command, try again... ")

input ('\n' + "End of program, press Enter to exit... ")
