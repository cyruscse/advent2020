#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")
   #f = open("puzzle_input_test.txt", "r")

   for line in f.read().split('\n'):
      puzzle_input.append(line)

   f.close()

   #print (puzzle_input)

   return list(filter(None,puzzle_input))


def executeLoop(puzzle_input):
    accumulator = 0
    visitedIndexes = []

    i = 0
    while i < len(puzzle_input):
        #check if index has been visited
        if i in visitedIndexes:
            print("Revisiting index: " + str(i))
            break

        #Mark that we visited this index
        visitedIndexes.append(i)

        #Get operation
        operation = puzzle_input[i].split(" ")[0]
        value = int(puzzle_input[i].split(" ")[1])
        #print(puzzle_input[i].split(" "))

        if (operation == "nop"):
            i += 1
            continue

        if (operation == "jmp"):
            i += value
            continue
            
        if (operation == "acc"):
            accumulator += value

        i += 1    

    return accumulator            

def main():
   puzzle_input = populate()

   accumulator = executeLoop(puzzle_input)

   print("Accumulator: " + str(accumulator))

if __name__ == "__main__":
   main()
