import sys
import random
import datetime
import calendar
import time
import os


def ask_and_compare(correct_ans):
    ans = input("what comes next...")
    if int(ans) == correct_ans:
        print("hurray!")
    else:
        print("Sorry..it is ", correct_ans)


def ask_to_continue():
    to_continue = input("Continue to play[y/n]:")
    if to_continue == "y":
        return 0
    elif to_continue == "n":
        return 1


def ask_math_question_using_dict(analogy_dict):
    analogy_keys = sorted(analogy_dict.keys())
    analogy_qn_key = random.randint(2, len(analogy_keys)-1)
    print("analogy_qn_key:", analogy_qn_key)
    first_key = analogy_keys[0]
    second_key = analogy_keys[1]
    print("If ", analogy_keys[0], "::", analogy_dict[analogy_keys[0]],
          "and ", analogy_keys[1], "::", analogy_dict[analogy_keys[1]],
          "then", analogy_keys[analogy_qn_key], "::")
    ans = input("")
    correct_ans = analogy_dict[analogy_keys[analogy_qn_key]]
    if int(ans) == correct_ans:
        print("hurray!")
    else:
        print("Sorry it is ", correct_ans)


def ask_set_questions(oper,set1, set2, correct_ans):
    """ Ask questions on operation oper related to sets of things"""
    print( "Here are the seat numbers that are available in bus number 1:",
        set(set1) )
    print( "Here are the seat numbers that are available in bus number 2:",
        set(set2) )
    print("Take a moment to read them carefully!")
    time.sleep(10)
    print( "Here come the questions...")
    time.sleep(2)
    os.system('cls')
    set_qn = { "and": "in both buses[empty if none match]: ",
               "or": "in one or the other bus[empty if none match]: ",
               "xor": "in one, but not both buses[empty if none match]: "}
    qn_str = """Can you tell which seat numbers, separated by commas,
             are free """+ set_qn[oper]
    ans_str = input(qn_str)
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
    print (i["passage"])
    time.sleep(10)
    print( "Here come the questions...")
    time.sleep(2)
    os.system('cls')
    qns = i["questions"]
    qn_keys = sorted(qns.keys())
    num_qns = len(qn_keys)
    time_now = int(time.time())
    remainder = time_now % num_qns
    qn = qn_keys[remainder]
    ans = input(qn)
    if ans.lower() == qns[qn_keys[remainder]].lower():
        print("hurray")
    else:
        print("Sorry it is",qns[qn_keys[remainder]] )
