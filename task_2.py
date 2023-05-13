oper_fp = "dataset/task1_2_operations.txt"
nums_fp = "dataset/task1_2_numbers.txt"


def main():
    pass

def oper_sel(oper,num):
    if oper == "1":
        # search
        search(num)
    elif oper == "2":
        # insert
        insert(num)
    elif oper == "3":
        # delete
        delete(num)
    else:
        return 404

def search(num):
    return position

def insert(num):
    return error

def delete(num):
    return error    

def auto_oper():
    oper_file = open("dataset/task1_2_operations.txt")
    line_count = oper_file.readlines()
    i = 0
    for i<line_count:
        line = oper_file.readline(1)
        word = line.split(" ")
        # word[0] is operation 
        # word[1] is the number
        result = oper_sel(word[0],word[1])
        
        i++

    pass