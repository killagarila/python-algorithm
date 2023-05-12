# imports



# Sorting Algorithms 

def main():
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
