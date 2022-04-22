import random

print("Larry June Phrase Generator\n")

def selection():
    sel = input("\nMake selection \n1: Generic Larry June Phrase\n2: \"Don't check me phrase\"\n : ")
    if(not sel.isnumeric()):
        clearConsole()
        print("You didn't make a selection")
        selection()
    sel = int(sel)
    if(sel in choices.keys()):
        choices[sel]()
    else:
        clearConsole()
        print("Choose a valid option")
        selection()

def clearConsole():
    print("\033[H\033[2J")

def gen():
    count = int(input("How many phrases do you want to generate?\n : "))
    print("")
    first  = ["Good Job ","Organic ","Very Peaceful ","Whats hat'nin ","Expensive ","Orange ","Green ", "24k ","Fresh "]
    second = ["chair ", "book ", "Corvette ", "smoothies ","juice ","tangerine juice ","biking ","plants ","miracles ","numbers ","income ","interest rates ","fatherhood ",""]
    last   = ["Yeehee ","you're doing good ","yessuh ","sockittome ","at midnight","Got Damn! ","in Dallas","in Vegas","in Frisco","in Sausalito","in Maryland","in 1991","aye aye aye","keep going!",""]
    for i in range(count):
        out = str(random.choice(first)) + str(random.choice(second)) + str(random.choice(last))
        print(out)
    reselect()
    

def check():
    count = int(input("How many phrases do you want to generate?\n : "))
    print("")
    first = "Dont check me, bitch "
    second = ["check that mileage","your interest rate","your engine light","the air quality"]
    for i in range(count):
        out = first + str(random.choice(second))
        print(out)
    reselect()

def reselect():
    choice = str(input("\nGo again? (y/n)\n : ")).lower()
    if(not choice):
        print("Make a selection")
        reselect()
    if(choice == "y" or choice == "yes"):
        clearConsole()
        selection()
    elif(choice == "n" or choice == "no"):
        clearConsole()
        print("Exit status 0")
        exit()
    else:
        print("Make a valid selection")
        reselect()

choices = {
    1: gen,
    2: check
}

selection()
