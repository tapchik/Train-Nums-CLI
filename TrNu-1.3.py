from random import randint as rand

post = [1, 0]
quiting = False
sot = ["addition ", "subtraction", "max sum", "way", "correct", "incorrect", "skipped"]
alright = False
saving = [True, False]

print ("""Start of program...

Train Nums supports user commands. You can enter command when user input is prompted: 

"skip" - skip difficult problems (counts by statistics);
"settings" - change difficulty;
"status" - show settings and your statistics;
"delete progress" - clear your statistics and start fresh;
"turn on/off addition";
"turn on/off subtraction";
"exit" - quit Train Nums. \n""")

try:
    blok = open ("TrNuSettings.txt", "r")
    allsod = (blok.readlines())
    for i in range(4):
        if allsod[i].endswith ("\n"):
            ling = len(allsod[i])
            sot[i] = int ((allsod[i])[:ling-1])
        else:
            sot[i] = int (allsod[i])
    blok.close()
except (NameError, FileNotFoundError, ValueError, IndexError):
    print ("File TrNuSettings.txt not found... ")
    
if (((sot[0] == 1) or (sot[0] == 0)) and
    ((sot[1] == 1) or (sot[1] == 0)) and
    ((sot[3] == 1) or (sot[3] == 2) or (sot[3] == 3)) and
    (sot[2] > 0)):
        alright = True
        post[0] = sot[0]
        post[1] = sot[1]
        mol_1 = sot[2]
        way = sot[3]

if alright == False:
    print ("File TrNuSettings.txt is corrupted. Set settings to default?")
    anss = input ("User input (y/n): ")
    anss = anss.lower()
    if (anss == ('yes')) or (anss == ('y')):
        blok = open ("TrNuSettings.txt", "w")
        blok.write ("1" + "\n" +
                    "0" + "\n" +
                    "25" + "\n" +
                    "1")
        blok.close()
        post[0] = int (1)
        post[1] = int (0)
        mol_1 = int (25)
        way = int (1)
    else:
        quiting = True

        
try:
    res = open ("TrNuStatistics.txt", "r")
    stats = (res.readlines())
    for i in range(3):
        if stats[i].endswith ("\n"):
            ling = len(stats[i])
            sot[4+i] = int ((stats[i])[:ling-1])
        else:
            sot[4+i] = int (stats[i])
    res.close()
except (FileNotFoundError):
    res = open ("TrNuStatistics.txt", "w")
    res.write ("0" + "\n" + "0" + "\n" + "0")
    res.close()
    print ("File TrNuStatistics.txt not found. New file was created. ")
    for i in range(3):
        sot[4+i] = 0
except (NameError, ValueError, IndexError):
    print ("File TrNuStatistics.txt is corrupted. Statistics are set to default. ")
    for tryi in range(3):
        sot[4+i] = 0
if (sot[4] < 0) or (sot[5] < 0) or (sot[6] < 0):
    print ("File TrNuStatistics.txt is corrupted. Statistics are set to default. ")
    sot[4] = 0
    sot[5] = 0
    sot[6] = 0   


#FUNCTIONS
def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def settings (x):
    while True:
        try:
            x = int (input('\n' + "Enter new max sum: "))
            break
        except ValueError:
            print ("Number is required, try again... ")
    return x

while True:
    if quiting == True:
        break    
    s = rand (1, mol_1)
    a = rand (1, s)
    b = s - a
    if (post[0] == 0) and (post[1] == 0):
        way = 3
        print ('\n' + "Addition and subtraction are turned off, generation is stopped... ")
    if (post[0] == 1) and (post[1] == 1):
        way = rand(1, 2)
    if (way == 1):
        print (' ')
        prim = print (a, '+', b)
        prim = (str (a) + ' + ' + str (b))
    elif (way == 2):
        print (' ')
        print (s,  '-', b)
        prim = (str (s) + ' - ' + str (b))

    while True:
        if quiting == True:
            break
        ans = (input("User input: "))
        try:
            ans = int (ans)
        except ValueError:
            ans = str (ans.lower())
        if (way == 1) and (ans == (a+b)):
            print ("Correct!")
            sot[4] += 1
            break
        elif (way == 2) and (ans == (s-b)):
            print ("Correct!")
            sot[4] += 1
            break
        elif (isint(ans)):
            sot[5] += 1
            print ("Incorrect, try again\n" + "\n" + prim)

        elif ans == ("exit"):
            while True:
                if saving[0] == True:
                    print ("\n" + "Save settings before leaving?")
                    wha1 = (input ("User input (y/n): "))
                    wha1 = (wha1.lower())
                    if (wha1 == ("yes")) or (wha1 == ('y')):
                        saving[0] = False
                        saving[1] = True
                        blok = open ("TrNuSettings.txt", "w")
                        blok.write (str(post[0]) + "\n" +
                                    str(post[1]) + "\n" +
                                    str(mol_1) + "\n" +
                                    str (way))
                        blok.close()
                    elif (wha1 == ("n")) or (wha1 == ("no")):
                        saving[0] = False
                        saving[1] = True
                    else:
                        print ("Wrong input. Try again... ")
                if saving [1] == True:
                    print ("\n" + "Save statistics?")
                    wha2 = (input ("User input (y/n): "))
                    wha2 = (wha2.lower())
                    if (wha2 == ("yes")) or (wha2 == ('y')):
                        res = open ("TrNuStatistics.txt", "w")
                        res.write (str(sot[4]) + "\n" +
                                   str(sot[5]) + "\n" +
                                   str(sot[6]))
                        res.close()
                        quiting = True
                        break
                    elif wha2 == ("no") or (wha2 == ("n")):
                        quiting = True
                        break        
                    else:
                        print ("Wrong input. Try again... ")

        elif ans == ("settings"):
            mol_1 = settings (mol_1)
            break

        elif ans == ("skip"):
            print ("We will count that. Next problem... ")
            sot[6] += 1
            break
    
        elif ans == ("turn on subtraction"):
            if way == 3:
                way = 2
            post[1] = 1
            break

        elif ans == ("turn off subtraction"):
            way = 1
            post[1] = 0
            break

        elif ans == ("turn on addition"):
            if way == 3:
                way = 1
            post[0] = 1
            break

        elif ans == ("turn off addition"):
            way = 2
            post[0] = 0
            break

        elif ans == ("delete progress"):
            sot[4] = 0
            sot[5] = 0
            sot[6] = 0
            print ("Your statistics were succesfully cleared... ")
            break
        
        elif ans == ("status"): 
            print ("Max sum: ", mol_1)
            if post[0] == 1:
                print ("Addition is turned on")
            elif post[0] == 0:
                print ("Addition is turned off")
            if post[1] == 1:
                print ("Subtraction is turned on")
            elif post[1] == 0:
                print ("Subtraction is turned off")
            print ("Solved problems total: {0}; {1} of them correctly, {2} incorrectly and {3} were skipped".format(sot[4]+sot[5]+sot[6], sot[4], sot[5], sot[6]))
            try:
                print ("{0}% of all problems are solved correctly".format(round(sot[4]/(sot[4]+sot[5]+sot[6])*100, 2)))
            except (ZeroDivisionError):
                print ("Statistics are not available")
            print ("\n" + "Back to the problem... ")
            

        else:
            print ("Unknown command, try again... ")

input ("End of program, press Enter to exit... ")
