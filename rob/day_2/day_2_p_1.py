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
      minimumOccurrence = password[0].split("-")[0]
      maximumOccurrence = password[0].split("-")[1]
      print ("Password range " + password[0] + ", character " + password[1][0] + ", and password " + password[2])
      for y in range(0, len(password[2])):
         if (char == password[2][y]):
            occurrence += 1
      if occurrence >= int(minimumOccurrence) and occurrence <= int(maximumOccurrence):
         validPassCount += 1

   return validPassCount




def main():
   puzzle_input = populate()

   validPassCount = countValidPasswords(puzzle_input)

   print("Valid password count: " + str(validPassCount))

if __name__ == "__main__":
   main()
