


# Stat Calculation function

# things to do 
# calculate a pokemon hp stat value 
# calculate pokemon's othe rhp

from logging import _Level


def statCalc(): 
    #HP stat value 
    print("please enter the base hp stat of the pokemon")
    base = int(input())

    print("please enetr the individual value | between 0-31")
    iv = int(input())

    print("please enter effort value | between 0-255 ")
    ev = int(input())

    print("pelase enter the target level")
    level = int(input())

    



# ENV Calculation function 
def envCalc():
    print(" I am going to calc env")

#option for the type of the calculation 
def start():  
    print("Please chose the type of tyhe calculation")
    print("1. Stat calculation")
    print("2. Env calculation")
    type = int(input("Select: "))

    if type == 1:
        statCalc()
    elif type == 2:
        envCalc()
    else: 
        print("wrong input")
