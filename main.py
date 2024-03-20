import random

    
print("")
print("Welcome to the Dice Rolling Simulator")
print("--------------------------------------")
print("")

def roll_dice():
    """
    Simulates rolling two dice and prints the results.

    This function simulates the action of rolling two six-sided dice. It uses
    ASCII art to represent each face of the dice. When the function is called,
    it prompts the user to roll the dice. After rolling, it displays the 
    outcome of each dice using ASCII art. The user is then asked if they would
    like to roll again, continuing until the user opts out.

    Parameters:
    None

    Returns:
    None: The function prints the outcome of each roll and does not return a value.
    """
        
    dice_drawing = {
        1: (
            " ------- ",
            "|       |",
            "|   o   |",
            "|       |",
            " ------- "
        ),
        2: (
            " ------- ",
            "| o     |",
            "|       |",
            "|     o |",
            " ------- "
        ),
        3: (
            " ------- ",
            "| o     |",
            "|   o   |",
            "|     o |",
            " ------- "
        ),
        4: (
            " ------- ",
            "| o   o |",
            "|       |",
            "| o   o |",
            " ------- "
        ),
        5: (
            " ------- ",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            " ------- "
        ),
        6: (
            " ------- ",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            " ------- "
        )
    }

    roll = input("Roll the dice? (Yes/No): ")
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("")
        print("Dice Results: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        print("")
        roll = input("Would you like to roll again? (Yes/No): ")
        print("")

roll_dice()