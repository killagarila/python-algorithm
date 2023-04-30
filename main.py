/* imports */
from datetime import datetime
import pandas as pd
import numpy as np

/* Test and Basic Functions */
def how_long(func):
    start = datetime.now()
    try:
        func()
    else:
        print("Error: Function Failed\n")
    end = datetime.now()
    length = end - start
    func_str = str(func)
    print(f"{func_str} : {length} seconds\n" )
    return length

def read_file(file):
    rf = pd.read_csv("..\\readables\\" + file)
    return rf

/* Sorting Algorithms */
def quick_sort(nums_file):
    nums = read_file(nums_file)

def bubble_sort(nums_file):
    pass

def merge_sort(nums_file):
    pass

def test_func(time):
    sleep(time)
    
how_long(test_func(5))