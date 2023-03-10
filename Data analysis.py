import re

def main ():
    # choose our file, output file, and person taking survey
    input1 = input("Enter a file: ")
    input2 = input("Choose output destination: ")
    p = input("Count: ")

    
    count = 0
    list1 = []
    file1 = open(input1, "r")
    f = file1.readlines()
    for line in f:
        # take away "/n" from list and also take away empty list
        rer = line.strip()
        rer1 = re.split(r'[?.]', rer)
        if rer1 != ['']:
            # 2D list created to separate score from survey question
            list1.append(rer1)
   
    for i in range(len(list1)):
        # gather and add up score
        # greater score -> shows bias in individual
        c = int(list1[i][1])
        count += c
        
    file1.close()
    out = open(input2, "a")
    out.write(f'{p}: {count} \n')
    out.close()
    
main()
