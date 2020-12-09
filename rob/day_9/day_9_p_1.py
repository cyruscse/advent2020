#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")
   #f = open("puzzle_input_test.txt", "r")

   for line in f.read().split('\n'):
      puzzle_input.append(line)

   f.close()

   print (puzzle_input)

   return list(filter(None,puzzle_input))


def findFirstInvalidNumber(puzzle_input):
    firstInvalidNumber = 0

    for i in range (25, len(puzzle_input)):
    #for i in range (5, len(puzzle_input)):
        isValid = False
        for j in range(i-25,i):
            for k in range(j+1,i):
                if j != k:
                    if int(puzzle_input[j]) + int(puzzle_input[k]) == int(puzzle_input[i]):
                        #print("Number: " + puzzle_input[i] + " made sum by: " + puzzle_input[j] + " and " + puzzle_input[k])
                        isValid = True
                        continue
        if isValid != True:
            firstInvalidNumber = int(puzzle_input[i])


    return firstInvalidNumber


def main():
   puzzle_input = populate()

   firstInvalidNumber = findFirstInvalidNumber(puzzle_input)

   print("First invalid number: " + str(firstInvalidNumber))

if __name__ == "__main__":
   main()
