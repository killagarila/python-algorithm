import time
import os
import bisect

oper_fp = "dataset/task1_2_operations.txt" # file path for automatic operations
nums_fp = "dataset/task1_2_numbers.txt" # file path for the number dataset
absolute_path = os.path.dirname(os.path.abspath(__file__))


def main():
    f = open(os.path.join(absolute_path, "dataset/task1_2_numbers.txt"), "r")
    line = f.read()
    f.close()
    list = [int(x) for x in line.split(' ')]
    start = time.time()
    sorted_list = classic_quick_sort(list)
    end = time.time()
    print(f"Time Taken - {str(end-start)}")
    
    start = time.time()
    sorted_list = auto_oper(sorted_list)
    end = time.time()
    print(f"Time Taken - {str(end-start)}")
    with open(("outputs/task_2_output.txt"),"w") as wf:
        for y in range(len(sorted_list)):
            wf.write(str(sorted_list[y]) + " ")

def classic_quick_sort(list):
    length = len(list)
    if length < 2:
       return list
    else:
        partition(list, 0, length-1)
        return list

def partition(list, lb, rb):    
    if rb-lb <= 1:
        return
    else:
        pivot = rb
        left = lb
        right = rb-1
        left2right = True
        while left <= right:
            if left2right:
                if list[left] > list[pivot]:
                    list[left], list[pivot] = list[pivot], list[left]
                    pivot = left
                    left2right = False
                left += 1
            else:
                if list[right] <list[pivot]:
                    list[right], list[pivot] = list[pivot], list[right]
                    pivot = right
                    left2right = True
                right -= 1
        partition(list,lb, pivot-1)
        partition(list, pivot+1, rb)

def oper_sel(list,oper,num):
    if oper == "1":
        # search
        list,error = search(list,num)
        return list,error
    elif oper == "2":
        # insert
        list,error = insert(list,num)
        return list,error
    elif oper == "3":
        # delete
        list,error = delete(list,num)
        return list,error
    else:
        return 404

def search(list, num): # 1
    try:
        position = list.index(int(num))
        error = f"Num in position {str(position)}"
        return list, error
    except ValueError:
            error = "Error: Num not found"
            return list, error

def insert(list, num): # 2
    x = 0
    try: 
        list.index(int(num))
        error = "Error: Num already in list"
        return list, error
    except ValueError:
        bisect.insort(list, int(num))
        error = "Num Inserted"
        return list,error

def delete(list, num): # 3
    try:
        list.index(int(num))
        list.remove(int(num))
        error = "Num Deleted"
        return list, error
    except ValueError:
        error = "Error: number not found in list"
        return list, error

def auto_oper(list):
    x = 0
    with open(os.path.join(absolute_path, "dataset/task1_2_operations.txt"), "r") as oper_file:
        oper_list = oper_file.read()
        oper_file.close()
    word = oper_list.split()
    new_list = list
    while x in range(int((len(word))/2)):
        new_list, error = oper_sel(new_list,word[x],word[x+1])
        # print(error) # uncomment to print off operation message
        x += 2
    return list


if __name__ == "__main__":
    main()