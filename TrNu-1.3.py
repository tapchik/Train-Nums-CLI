from random import randint as randint
from random import choice as choice
import json
import random

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
quit = False
# Detects change in operator again
# I am not seeing the full picture here
delta_operator = False

#SCRIPTS

def script_help ():
    print ("""Start of program...

Train Nums supports user commands. You can enter command when user input is prompted:

"skip" - skip difficult problems (counts by statistics);
"settings" - change difficulty;
"status" - show settings and your statistics;
"delete progress" - clear your statistics and start fresh;
"turn on/off addition";
"turn on/off subtraction";
"exit" - quit Train Nums. """)

def script_settings ():
    while True:
        try:
          x = int (input('\n' + "Enter new max sum: "))
          return (x)
        except ValueError:
          print ("Number is required, try again... ")

def script_show_status ():

  print ('\n' + "Max sum:", data["max sum"])

  if data["addition"] == True:
    print ("Addition is turned on")
  else:
    print ("Addition is turned off")



  if data["subtraction"] == True:
    print ("Subtraction is turned on")
  else:
    print ("Subtraction is turned off")
    
# I wanted to use non-binary variable but then
  # it would be confusing so, changing the value to True
  # solves our problem
  
  if (data["subtraction"] is True) ^ (data["addition"] is True):
    #solved = True
    operation = choose_operation()
    data["problem"], data["answer"] = generate_problem(operation)
    del operation
    solved = False

  if (data["subtraction"] is True) ^ (data["addition"] is True):
      
      total = data["correct"] + data["incorrect"] + data["skipped"]

  print ("Solved problems total: {0}; ".format(total), end='')
  print ("{0} of them correctly, ".format(data["correct"]), end='')
  print ("{0} incorrectly ".format(data["incorrect"]), end='')
  print ("and {0} were skipped".format(data["skipped"]))

  try:
    print ("{0}% of all problems are solved correctly.".format(round(data["correct"]/total*100), 2))
  except ZeroDivisionError:
    print ("Further statistics are not available")
    print ("\n" + "Back to the problem... ")

#FUNCTIONS

def file_read ():

  try:
    with open ("TrNuSettings.json", "r") as file:
      x = json.load(file)

      data["addition"] = x["addition"]
      data["subtraction"] = x["subtraction"]
      data["max sum"] = x["max sum"]
      data["problem"] = x["problem"]
      data["answer"] = x["answer"]
      data["correct"] = x["correct"]
      data["incorrect"] = x["incorrect"]
      data["skipped"] = x["skipped"]

      if (data["addition"] in [True, False]) and (data["subtraction"] in [True, False]) and (data["correct"] >= 0) and (data["incorrect"] >= 0) and (data["skipped"] >= 0) and (data["answer"] >= 0) and (data["max sum"] > 0):
            return True
      else:
          raise KeyError()

  except FileNotFoundError:
    print ("This is a first startup of Train Nums on this computer. ")
    print ("We love seeing new users! " + '\n')
    return False

  except KeyError:
    print ("Settings file must be currupted. Did you try to cheat? ")
    print ("Program is set to default settings and your progress was nullified. " + '\n')
    return False

def file_save ():
  with open ("TrNuSettings.json", "w") as file:
    json.dump (data, file, indent = 4)

def set_to_default ():

  data = {"addition": True,
          "subtraction": False,
          "max sum": 25,
          "current": [0, "+", 0, 0],
          "correct": 0,
          "incorrect": 0,
          "skipped": 0}

def choose_operation ():

  options = []

  if data["addition"] == True:
    options.append("+")
  if data["subtraction"] == True:
    options.append("-")

  if options != []:
    return choice(options)
  return None

def generate_problem (operation):

    problem = str()

    #example
    # 123     '+'      456  =  579
    #left, operation, right, answer

    if operation == '+':

        answer = randint (1, data["max sum"])
        left = randint (1, answer)
        right = answer - left

        problem += str(left)
        problem += ' ' + operation + ' '
        problem += str(right)

    elif operation == '-':

        left = randint (1, data["max sum"])
        right = randint (1, left)
        answer = left - right

        problem += str(left)
        problem += ' ' + operation + ' '
        problem += str(right)

    elif operation == None:
        # This means two things either the program should exit
        # or select randomly an operator
        problem, answer = generate_problem (random.choice(['+', '-']))
        #problem = None
        #answer = None

    return (problem, answer)

#START OF PROGRAM
#Nevermind

if file_read() == True:
    solved = False
    file_read()
else:
    solved = True
    set_to_default()

script_help()

while True:

    if quit == True:
        break

    if solved == True:
        operation = choose_operation()
        data["problem"], data["answer"] = generate_problem(operation)
        del operation
        solved = False

    print ('\n' + data["problem"])

    user = input("User input: ")

    try:
        user = int(user)
    except ValueError:
        user = str (user.lower())

    if user == data["answer"]:
        print ("Correct!")
        data["correct"] += 1
        solved = True

    elif isinstance(user, int):
        print ('\n' + "Incorrect, try again")
        data["incorrect"] += 1

    elif user == "exit":
        file_save()
        quit = True

    elif user == "settings":
        data["max sum"] = script_settings()
        print ("Back to math problem... ")

    elif user == "skip":
        print ("We will count that. Next problem... ")
        if state_change == 1:
            data["skipped"] += 1
        solved = True
        state_change = 0

    elif user == "turn on addition":
        state_change = 1
        if data["addition"] == True:
          print ('\n' + "Addition is already turned on")
        else:
          print ('\n' + "Addition is turned on now")
          data["addition"] = True
        print ("Back to math problem... ")

    elif user == "turn off addition":
        state_change = 1
        if data["addition"] == False:
          print ('\n' + "Addition is already turned off")
        else:
          print ('\n' + "Addition is turned off now")
          data["addition"] = False
        print ("Back to math problem... ")

    elif user == "turn on subtraction":
        state_change = 1
        if data["subtraction"] == True:
          print ('\n' + "Subtraction is already turned on")
        else:
          print ('\n' + "Subtraction is turned on now")
          data["subtraction"] = True
        print ("Back to math problem... ")

    elif user == "turn off subtraction":
        if data["subtraction"] == False:
          print ('\n' + "Subtraction is already turned off")
        else:
          print ('\n' + "Subtraction is turned off now")
          data["subtraction"] = False
        print ("Back to math problem... ")

    elif user == "delete progress":
        data["correct"] = 0
        data["incorrect"] = 0
        data["skipped"] = 0
        print ('\n' + "Your statistics were succesfully cleared... ")

    elif user == "status":
        script_show_status()

    elif user == "help":
        print (' ')
        script_help()

    else:
        print ('\n' + "Unknown command, try again... ")

input ('\n' + "End of program, press Enter to exit... ")
