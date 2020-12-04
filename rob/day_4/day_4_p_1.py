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

def countValidPassports(puzzle_input):
   count = 0
   for x in range(0, len(puzzle_input)):
      if ("byr:" in puzzle_input[x] and 
         "iyr:" in puzzle_input[x] and
         "eyr:" in puzzle_input[x] and
         "hgt:" in puzzle_input[x] and
         "hcl:" in puzzle_input[x] and
         "ecl:" in puzzle_input[x] and
         "pid:" in puzzle_input[x]):
         count += 1

   return count

def main():
   puzzle_input = populate()

   validPassports = countValidPassports(puzzle_input)

   print ("Valid passports: " + str(validPassports))

if __name__ == "__main__":
   main()
