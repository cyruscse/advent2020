#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   #f = open("puzzle_input_test.txt", "r")
   f = open("puzzle_input.txt", "r")
   for line in f:
      line = line.replace("\n","") 
      puzzle_input.append(line)

   f.close()

#   print (puzzle_input)
#   print (len(puzzle_input))

   return puzzle_input

def determineRow(rowBoarding):
    row = [x for x in range (0,128)]

    for i in range(0, 7):
        if (rowBoarding[i] == "F"):
            row = row[:(len(row)//2)]
        else:
            row = row[(len(row)//2):]

            
    return row[0]


           
def determineColumn(columnBoarding):
    column = [x for x in range(0,8)]

    for i in range(0,3):
        if (columnBoarding[i] == "L"):
            column = column[:(len(column)//2)]
        else:
            column = column[(len(column)//2):]
            

    return column[0]        
            

def determineSeatID(boardingPass):
    seatID = 0
    rowBoarding = ""
    columnBoarding = ""
    for i in range(0,7):
        rowBoarding += boardingPass[i]
        
    for i in range(7,10):
        columnBoarding += boardingPass[i]


    #print("Row boarding: " + rowBoarding + " Column Boarding: " + columnBoarding)    

    row = determineRow(rowBoarding)
    column = determineColumn(columnBoarding)

    #print("Row: " + str(row) + " , Column: " + str(column))

    seatID = (row * 8) + column

    return seatID


def main():
   puzzle_input = populate()

   highestSeatID = 0

   for i in puzzle_input:
       seatID = determineSeatID(i)
       if seatID >= highestSeatID:
           highestSeatID = seatID
   
   print("Highest Seat ID: " + str(highestSeatID))
   


if __name__ == "__main__":
   main()
