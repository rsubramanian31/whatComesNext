# Program to play a simple game of what comes next.
# Has easy, medium, hard levels.

import sys
import random
import datetime
import calendar
import time
import mathematical_functions
import verbal_functions
import analogy_functions
import user_interaction_functions

# main function
if len(sys.argv) == 1:
    print(" Hello and figure out what comes next")
    print("""
    1. easy
    2. medium
    3. hard
    """)
    difficulty = input("Please choose [1/2/3]:")
    if int(difficulty) in (1, 2, 3):
        continue_to_play = 0
        while continue_to_play == 0:
            if int(difficulty) == 1:
                mathematical_functions.ap(2, 5)
                verbal_functions.comprehension_test()
            elif int(difficulty) == 2:
                puzzle_choice = {1: mathematical_functions.gp,
                                 2: mathematical_functions.ap}
                choice = random.randint(1, len(list(puzzle_choice.keys())))
                puzzle_choice[choice](3, 10)
                mathematical_functions.set_ops()
            elif int(difficulty) == 3:
                # puzzle_choices = ["expo"]
                analogy_functions.analogies()
                mathematical_functions.expon(3, 15)
                mathematical_functions.root_calc(4)
            continue_to_play = user_interaction_functions.ask_to_continue()
        else:
            print("\n Thank you for playing. Hope you enjoyed the game\n")
    else:
        print("Invalid input\n")
