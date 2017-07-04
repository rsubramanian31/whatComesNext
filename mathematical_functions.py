import sys
import random
import datetime
import calendar
import time
import os
import user_interaction_functions


def ap(m, n):
    """function to provide an arithmetic progression. Takes 2 args:
    m: starting number, n: range for step """
    step = random.randint(1, n)
    print(m, m+step, m+2*step)
    correct_ans = m+3*step
    user_interaction_functions.ask_and_compare(correct_ans)


def gp(m, n):
    """function to provide an geometric progression. Takes 2 args:
    m,n: range to choose multiplier. starting_num is a random number"""
    multiplier = random.randint(m, n)
    start_num = random.randint(1, 20)
    print(start_num, start_num * multiplier, start_num * (multiplier ** 2))
    correct_ans = start_num * (multiplier ** 3)
    user_interaction_functions.ask_and_compare(correct_ans)


def expon(m, n):
    """function to calculate exponent. takes 2 arguments:
    m: exponent, n: range of numbers raised to the power m.
    This way, medium difficulty can use numbers from smaller range.
    For eg., expon(3,5) means choose a number between 2,5 and raise
    it to power 3 and use that to ask questions."""
    m_expon = {x: x ** m for x in range(2, n)}
    user_interaction_functions.ask_math_question_using_dict(m_expon)


def root_calc(m):
    """function to calculate mth root, given m """
    m_roots = {x ** m: x for x in range(2, 10)}
    user_interaction_functions.ask_math_question_using_dict(m_roots)


def set_ops():
    """function to do standard set operations"""

    # defining a couple of sets
    free_seats_1 = {str(random.randint(1, 20)), str(random.randint(1, 20)),
                    str(random.randint(1, 20))}
    free_seats_2 = {str(random.randint(1, 20)), str(random.randint(1, 20)),
                    str(random.randint(1, 20))}
    # using or, and, xor functions
    user_interaction_functions.ask_set_questions(
                        "or",
                        free_seats_1,
                        free_seats_2,
                        set(free_seats_1 | free_seats_2))

    user_interaction_functions.ask_set_questions(
                        "and",
                        free_seats_1,
                        free_seats_2,
                        set(free_seats_1 & free_seats_2))

    user_interaction_functions.ask_set_questions(
                        "xor",
                        free_seats_1,
                        free_seats_2,
                        set(free_seats_1 ^ free_seats_2))
