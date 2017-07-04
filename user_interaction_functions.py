import sys
import random
import datetime
import calendar
import time
import os


def ask_and_compare(correct_ans):
    """ Function to take user input, compare with correct answer """
    ans = input("what comes next...")
    if int(ans) == correct_ans:
        print("hurray!")
    else:
        print("Sorry..it is ", correct_ans)


def ask_to_continue():
    """ Function to query user to continue or quit """
    to_continue = input("Continue to play[y/n]:")
    if to_continue == "y":
        return 0
    elif to_continue == "n":
        return 1


def ask_math_question_using_dict(math_dict):
    """ Function to take a dict and ask math questions """
    math_keys = sorted(math_dict.keys())
    math_qn_key = random.randint(2, len(math_keys)-1)
    first_key = math_keys[0]
    second_key = math_keys[1]
    print("If ", math_keys[0], "::", math_dict[math_keys[0]],
          "and ", math_keys[1], "::", math_dict[math_keys[1]],
          "then", math_keys[math_qn_key], "::")
    ans = input("")
    correct_ans = math_dict[math_keys[math_qn_key]]
    if int(ans) == correct_ans:
        print("hurray!")
    else:
        print("Sorry it is ", correct_ans)


def ask_set_questions(oper, set1, set2, correct_ans):
    """ Ask questions on operation oper related to sets of things"""
    print("Here are the seat numbers that are available in bus number 1:",
          set(set1))
    print("Here are the seat numbers that are available in bus number 2:",
          set(set2))
    print("Take a moment to read them carefully!")
    # giving time for user to read the sets
    time.sleep(10)
    print("Here come the questions...")
    time.sleep(2)
    os.system('cls')
    set_qn = {"and": "in both buses[empty if none match]: ",
              "or": "in one or the other bus[empty if none match]: ",
              "xor": "in one, but not both buses[empty if none match]: "}
    qn_str = """Can you tell which seat numbers, separated by commas,
             are free """ + set_qn[oper]
    ans_str = input(qn_str)
    # providing an option for user to enter no matches with empty
    if ans_str == "empty":
        ans_in_set = set()
    else:
        # split ans by comma into words and make into set
        ans_split = ans_str.split(",")
        ans_in_set = set(ans_split)
    print("You answered:", ans_in_set)
    if ans_in_set == correct_ans:
        print("hurray!")
    else:
        print("sorry it is", correct_ans)


def ask_comprehension_qns(i):
    """Takes a passage and a set of questions related to the
        passage and asks them randomly"""
    print("\n Take a moment to read the passage carefully!\n\n")
    print(i["passage"])
    time.sleep(10)
    print("Here come the questions...")
    time.sleep(2)
    os.system('cls')
    qns = i["questions"]
    qn_keys = sorted(qns.keys())
    num_qns = len(qn_keys)
    # a simple random function to choose key for question
    time_now = int(time.time())
    remainder = time_now % num_qns
    qn = qn_keys[remainder]
    ans = input(qn)
    # converting to lower case before comparing
    if ans.lower() == qns[qn_keys[remainder]].lower():
        print("hurray")
    else:
        print("Sorry it is", qns[qn_keys[remainder]])
