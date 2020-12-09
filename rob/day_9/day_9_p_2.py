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


def determineEncryptionWeakness(puzzle_input, invalidNumber):

    for i in range (0, len(puzzle_input)):
        contigSum = int(puzzle_input[i])
        for j in range(i+1,len(puzzle_input)):
           contigSum += int(puzzle_input[j])
           if contigSum == invalidNumber:
              contigList = puzzle_input[i:j]
              print("Found a contig list for invalid number: " + str(invalidNumber))
              print(contigList)
              print("Min: " +  min(contigList) + ", Max: " + max(contigList))
              contigList.sort()
              return int(contigList[0]) + int(contigList[len(contigList)-1])
           elif contigSum >= invalidNumber:
              break





def main():
   puzzle_input = populate()

   encryptionWeaknessNumber = determineEncryptionWeakness(puzzle_input, 731031916)

   print("Encryption weakness number: " + str(encryptionWeaknessNumber))

if __name__ == "__main__":
   main()
