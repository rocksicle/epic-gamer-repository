'''
Checkerboard.py
Mr.Price

'''

import argparse


parser = argparse.ArgumentParser(description="Input values to make a checkerboard of characters")
parser.add_argument("rows", type=int, help="number of rows in the checkerboard")
parser.add_argument("columns", type=int, help="number of columns in the checkerboard")
parser.add_argument("start_char", type=str, help="Character in the alphabet to start on")
parser.add_argument("cycle_size", type=int, help="amount of characters to cycle through after starting character")
parser.add_argument("width", type=int, help="amount of times to repeat each character")

args = parser.parse_args()

def iterateChar(sc, it):
    """
    Iterator iterates the starting character.
    """
    rv = ord(sc)
    rv += it
    rv = chr(rv)
    return rv

def checkerboard(rows,columns,start_char,cycle_size,width):
    counter=0
    to_print=list("")
    to_print_holder=""
    counter2=0
    counter3=0
    counter4=0
    counter5=0
    counter6=0

    while(counter<cycle_size):

        while(counter5<width):
            to_print_holder+=iterateChar(start_char,counter)
            counter5+=1

        counter+=1
        to_print.append(to_print_holder)
        to_print_holder=""
        counter5=0

    if(columns>cycle_size):
        while(counter4<(columns-cycle_size)):

            while(counter2<width):
                to_print_holder+=iterateChar(start_char,counter3)
                counter2+=1
            
            counter2=0
            counter3+=1
            to_print.append(to_print_holder)
            counter4+=1
            to_print_holder=""

    while(rows>0):
        for j in range(width):
            for i in to_print:
                print(i,end="")
            print()

        rows-=1
        to_print.append(to_print[counter6])
        to_print[counter6]=""
        counter6+=1

    
    


    


# checkerboard(rows,columns,start_char,cycle_size)
checkerboard(args.rows, args.columns,args.start_char,args.cycle_size,args.width)




