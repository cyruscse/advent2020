#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   #f = open("puzzle_input_test.txt", "r")
   f = open("puzzle_input.txt", "r")
   for line in f.read().split("\n\n"):
      puzzle_input.append(line)

   f.close()

   #print (puzzle_input)

   return puzzle_input

def countYesEveryoneQuestions(puzzle_input):

   totalCount = 0

   for i in range(0,len(puzzle_input)):
       group = puzzle_input[i].split('\n')
       group = list(filter(None,group))
       yesQuestions = []
       #Count how many unique yes questions are there
       for j in range(0, len(group)):
           for char in group[j]:
               if char not in yesQuestions:
                   yesQuestions.append(char)

       #print(yesQuestions)
       yesQuestionsEveryone = []
       for k in range(0, len(yesQuestions)):
           inEveryone = True
           for j in range(0, len(group)):
               #print ("Yes questions: " + yesQuestions[k] + " in group: " + group[j])
               if yesQuestions[k] not in group[j]:
                   inEveryone = False
           if inEveryone:
               yesQuestionsEveryone.append(yesQuestions[k])
       #print(yesQuestionsEveryone)        
       totalCount += len(yesQuestionsEveryone)

   return totalCount 


def main():
   puzzle_input = populate()

   totalCount = countYesEveryoneQuestions(puzzle_input)

   print("Total Count: " + str(totalCount))


if __name__ == "__main__":
   main()
