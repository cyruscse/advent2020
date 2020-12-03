#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")

   for line in f:
      puzzle_input.append(int(line))

   f.close()

   #print (puzzle_input)

   return puzzle_input


def product2020(puzzle_input):
   for i in range (0, len(puzzle_input)):
      for j in range (0, len(puzzle_input)):
         if (puzzle_input[i] + puzzle_input[j] == 2020):
            print("Found " + str(puzzle_input[i]) + " and " + str(puzzle_input[j]) + " which add up to 2020")
            return puzzle_input[i] * puzzle_input[j]


def main():
   puzzle_input = populate()

   product = product2020(puzzle_input)
   print ("Product: " + str(product))

if __name__ == "__main__":
   main()
