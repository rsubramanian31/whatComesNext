import sys
import random
import datetime
import calendar
import time


def analogies():
    """function to setup some dictionaries and setup analogy questions"""

    capitals = {"India": "New Delhi",
                "USA": "Washington DC",
                "Canada": "Ottawa",
                "Mexico": "Mexico City",
                "Brazil": "Brasilia",
                "Australia": "Canberra",
                }
    currencies = {"India": "Rupee",
                  "USA": "Dollar",
                  "UK": "Pound",
                  "Mexico": "Peso",
                  "China": "Yuan",
                  }
    analogy_list = [capitals, currencies]
    print("\n Let us try some analogies\n")
    # a simple mod function on time to choose a dictionary to ask qns
    time_now = int(time.time())
    remainder = time_now % 2
    analogy_dict = analogy_list[remainder]
    # choose a random key to ask question, seed analogy is first key-val
    analogy_keys = sorted(analogy_dict.keys())
    analogy_qn_key = random.randint(1, len(analogy_keys)-1)
    # first_key is seed analogy
    first_key = analogy_keys[0]
    print("If ", first_key, "::", analogy_dict[first_key],
          "  ", analogy_keys[analogy_qn_key], "::")
    ans = input("")
    correct_ans = analogy_dict[analogy_keys[analogy_qn_key]]
    # converting to lower case to compare more liberally
    if ans.lower() == correct_ans.lower():
        print("hurray!")
    else:
        print("Sorry it is ", correct_ans)
