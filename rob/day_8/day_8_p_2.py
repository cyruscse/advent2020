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
            #print("Revisiting index: " + str(i))
            break

        #Mark that we visited this index
        visitedIndexes.append(i)

        #Get operation
        operation = puzzle_input[i].split(" ")[0]
        value = int(puzzle_input[i].split(" ")[1])
        #print(puzzle_input[i].split(" "))

        if (operation == "nop"):
            i += 1
            if i == len(puzzle_input):
                return(True, accumulator)

            continue

        if (operation == "jmp"):
            i += value
            if i == len(puzzle_input):
                return(True, accumulator)

            continue
            
        if (operation == "acc"):
            accumulator += value

        i += 1    
        if i == len(puzzle_input):
            print("found termination")
            return (True, accumulator)

    return (False, accumulator)           

def main():
   puzzle_input = populate()

   for i in range(0,len(puzzle_input)):
       operation = puzzle_input[i].split(" ")[0]
       value = puzzle_input[i].split(" ")[1]
       if (operation == "nop"):
           copyInput = puzzle_input.copy()
           copyInput[i] = "jmp " + value
           #print("Changing index: " + str(i) + " from nop to jmp")
           #print(copyInput[i])
           result = executeLoop(copyInput)
           if result[0] == True:
               print("Accumulator: " + str(result[1]))
               break

       elif (operation == "jmp"):
           copyInput = puzzle_input.copy()
           copyInput[i] = "nop " + value
           #print(copyInput[i])
           #print("Changing index: " + str(i) + " from jmp to nop")
           result = executeLoop(copyInput)
           if result[0] == True:
               print("Accumulator: " + str(result[1]))
               break

           

if __name__ == "__main__":
   main()
