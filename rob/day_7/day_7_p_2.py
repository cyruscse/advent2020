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

def countBagsInBag(bagName, puzzle_input):
    count = 0
    #Base case: if bag is any of these colours return 0
    if (bagName == "shiny purple" or 
        bagName == "striped teal" or
        bagName == "wavy brown" or 
        bagName == "dotted beige" or
        bagName == "muted fuchsia" or
        bagName == "dim gray" or 
        bagName == "dull magenta" or
        bagName == "light green" or
        bagName == "dark silver" or
        bagName == "light chartreuse"):
        return 0

    #search for bag in puzzle_input
    index = 0
    for i in range(0,len(puzzle_input)):
        bag = puzzle_input[i].split('bags contain')[0].strip()
        if bagName == bag:
            index = i
            break
    content = puzzle_input[index].split('bags contain')[1].replace(".","").replace("bags","").replace("bag","").strip()
    content = content.split(",")
    print(content)
    for j in range(0, len(content)):
        quantity = content[j].strip().split(" ")[0]
        contentBagName = content[j].strip().split(" ")[1] + " " + content[j].strip().split(" ")[2]
        print("Quantity: " + quantity + " , of Bag: " + contentBagName)
        count += int(quantity) + int(quantity)*countBagsInBag(contentBagName, puzzle_input) 

    return count

        

def main():
   puzzle_input = populate()

   count = countBagsInBag("shiny gold", puzzle_input)

   print("Count: " + str(count))

if __name__ == "__main__":
   main()
