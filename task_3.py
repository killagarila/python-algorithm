# imports 
from multiprocessing import Process,Manager
import time

# Test and Basic Functions 

def remchars(char):
    if char.isalnum() or char == ' ':
        return True
    else:
        return False

def name_in_text(names,text,rdic):
    for word in text:
        if word.lower() in names:
            rdic[word] = rdic.get(word,0) + 1
        
# Sorting Algorithms

if __name__ == '__main__':
    r1 = open(("dataset/task1_3_names.txt"),"r") # dataset for words to look for (in this case names)
    names = r1.read()
    r1.close()
    r2 = open(("dataset/task1_3_text.txt"),"r",errors="ignore") # dataset for text looking through
    text = r2.read()
    r2.close()

    man = Manager()
    nc = man.dict()
    new_text = ''.join(filter(remchars,text)) # remove invalid characters from text
    name_list = names.split("\n")
    name_list = list(map(str.lower,name_list))
    text_list = new_text.split(" ")
    half = int(len(text_list)/2)
    p1 = Process(target=name_in_text,args=(name_list,text_list[:half],nc))
    p2 = Process(target=name_in_text,args=(name_list,text_list[half:],nc))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    with open("outputs/task_3_output.txt", 'w') as f: 
        for key, value in nc.items():
            f.write('%s:%s\n' % (key, value))
