import random  # random is a python built-in module


def roll_dice():
    dice_side = random.randrange(1, 7)
    print(dice_side)


if __name__ == '__main__':
    roll_dice()
