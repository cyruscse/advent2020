#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")

   for line in f.read().split('\n'):
      puzzle_input.append(line)

   f.close()

   print (puzzle_input)

   return list(filter(None,puzzle_input))

def countBagsContainingShinyGoldBag(puzzle_input):
    count = 0
    shinyGoldBagContains = []
    shinyGoldBagContains.append("shiny gold")

    isDone = True

    while isDone:
        isDone = False
        for line in list(puzzle_input):
            bag = line.split('bags contain')[0].strip()
            contents = line.split('bags contain')[1].strip()
            #print(puzzle_input[i])
            print ("Bag: " + bag + ", Contents: " + contents)
            for j in range(0, len(shinyGoldBagContains)):
                if shinyGoldBagContains[j] in contents:
                    shinyGoldBagContains.append(bag)
                    isDone = True
                    puzzle_input.remove(line)
                    break
    
    count = len(shinyGoldBagContains) - 1

    return count

def main():
   puzzle_input = populate()

   count = countBagsContainingShinyGoldBag(puzzle_input)

   print("Count: " + str(count))

if __name__ == "__main__":
   main()
