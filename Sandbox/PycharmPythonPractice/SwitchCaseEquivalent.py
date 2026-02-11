"""
    switch(n)
    {
        case 0:
            print("You selected blue.");
            break;
        case 1:
            print("You selected yellow");
            break;
        case 2:
            print("You selected green");
            break;
"""

def PrintBlue():
    print("You choose blue!\r\n") # -- \r carriage return

def PrintRed():
    print("You choose red!\r\n")

def PrintOrange():
    print("You choose orange!\r\n")

def PrintYellow():
    print("You choose yellow!\r\n")

ColorSelect = {
    0: PrintBlue,
    1: PrintRed,
    2: PrintOrange,
    3: PrintYellow
}

Selection = 0
while(Selection != 4):
    print("0. Blue")
    print("1. Red")
    print("2. Orange")
    print("3. Yellow")
    print("4. Quit")
    Selection = int(input("Select a color option: "))
    if(Selection >=0 ) and (Selection < 4):
        ColorSelect[Selection]()