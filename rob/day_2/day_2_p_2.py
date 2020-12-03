#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")

   for line in f:
      puzzle_input.append(line)

   f.close()

   #for x in range(0,len(puzzle_input)):
   #   print (puzzle_input[x])

   return puzzle_input

def countValidPasswords(puzzle_input):
   validPassCount = 0

   for x in range(0, len(puzzle_input)):
      password = puzzle_input[x].split(" ")
      char = password[1][0]
      occurrence = 0
      position1 = password[0].split("-")[0]
      position2 = password[0].split("-")[1]
      print ("Position 1: " + position1 + ", Position 2: "+ position2 + ", character " + password[1][0] + ", and password " + password[2])
      if (char == password[2][int(position1)-1]):
         occurrence += 1
      if (char == password[2][int(position2)-1]):
         occurrence += 1
      if occurrence == 1:
         validPassCount += 1

   return validPassCount




def main():
   puzzle_input = populate()

   validPassCount = countValidPasswords(puzzle_input)

   print("Valid password count: " + str(validPassCount))

if __name__ == "__main__":
   main()
