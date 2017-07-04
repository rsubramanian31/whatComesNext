import sys
import random
import datetime
import calendar
import time
import user_interaction_functions
import os
import json


def comprehension_test():
    """ Function to test comprehension, given a short passage p"""
    # reading json file which has passages and the respective questions
    with open('passages.json') as passages_json:
        data = json.load(passages_json)
        for i in data["comprehension_passages"]:
            user_interaction_functions.ask_comprehension_qns(i)
