# imports 
import time as t
import pandas as pd
import numpy as np
import string
import re

# Test and Basic Functions 

def write_file(file,text):
    wf = open(("outputs/" + file + ".txt"),"a")
    wf.write(text)
    wf.close()
    print("Output in /outputs/" + file)

# Sorting Algorithms 
def task_1():
    r = open(("dataset/task1_1_numbers.txt"),"r")
    nums = r.read()
    r.close()
    num_list = nums.split(" ")
    nc = {}
# create dictionary with all numbers and how many times they appear in txt
    for num in num_list:
        if num in nc.keys():
            nc[num] +=1
        else:
            nc[num] = 1
    print(nc)

    # write_file("task_1_output",nums)

# def read_file_csv(file):
#     rf = pd.read_csv("..\\readables\\" + file)
#     return rf

# def read_file(file):
#     rf = open(("\\dataset\\" + file),"r")
#     rf.close()
#     return rf.read()

# def how_long(func):
#     start = t.time()
#     # try:
#     func()
#     # except:
#     #     print("Error: Function Failed\n")
#     end = t.time()
#     length = end - start
#     func_str = str(func)
#     print(f"{func_str} : {length} seconds\n" )
#     return length

# def test_func(time):
#     print("test")
#     t.sleep(time)
#     pass