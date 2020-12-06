#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")
   for line in f.read().split("\n\n"):
      puzzle_input.append(line)

   f.close()

   #print (puzzle_input)

   return puzzle_input

def countYesQuestions(puzzle_input):

   totalCount = 0

   for i in range(0,len(puzzle_input)):
       group = puzzle_input[i].split('\n')
       yesQuestions = []
       for j in range(0, len(group)):
           for char in group[j]:
               if char not in yesQuestions:
                   yesQuestions.append(char)
       totalCount += len(yesQuestions)

   return totalCount 


def main():
   puzzle_input = populate()

   totalCount = countYesQuestions(puzzle_input)

   print("Total Count: " + str(totalCount))


if __name__ == "__main__":
   main()
