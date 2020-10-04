import random 

def roll_dice(range):
    while True:
        dice_side = random.randrange(1, range)
        print("You rolled: " + str(dice_side))
        yes_or_no=input("Do you want to continue? y/n    ")
        if yes_or_no == 'n':
            print("Over!")
            break


if __name__ == '__main__':
    roll_dice(7)
