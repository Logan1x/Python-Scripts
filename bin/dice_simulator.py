import random 

def roll_dice():
    while True:
        dice_side = random.randrange(1, 7)
        print("No on the top of dice rolled is ",dice_side)
        yes_or_no=input("Do you want to continue y/n    ")
        if yes_or_no == 'n':
            print("Over !")
            break


if __name__ == '__main__':
    roll_dice()
