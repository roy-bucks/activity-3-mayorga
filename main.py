import stat_cal as stat

#This will compute the HP and the other stat
def stat_calc(): 
    print("I am going to calculate the HP and other stat")
    print("Please enter the following input")

    print("please enter the base hp")
    base = int(input())

    flag = 1
    while flag == 1:
        print("Please enter the IV between 0-31")
        iv = int(input())
        if(iv >= 0 and iv <= 31):
            flag = 2


    flag2 = 1
    while flag2 == 1:
        print("Please enter the EV between 0-255")
        ev = int(input())
        if(ev >= 0 and ev <= 255):
            flag2 = 2

    print("please enter the level")
    level = int(input())


    stat_data = {
        "base": base,
        "iv": iv,
        "ev": ev,
        "level": level
    }

    total_hp = stat.compute.hp(stat_data)
    print("The total hp is: ")
    print(total_hp)

def ev_calc(): 
    print("I am goint to ev calc")
    


#First step1
#user chose between ev calculation and stat calculation 
def start():
    print("Please choose type of calculation")
    print("1. Stat calculation")
    print("2. Ev calculation")

    opt = int(input())

    if(opt == 1):
        stat_calc()

    elif(opt == 2):
        ev_calc()

    else:
        print("Invalid input") 



start()
