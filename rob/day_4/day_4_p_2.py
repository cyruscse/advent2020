#!/usr/bin/python3

from array import *
import re

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")
   #f = open("puzzle_input_test.txt", "r")
   for line in f.read().split("\n\n"):
      puzzle_input.append(line)

   f.close()

   #print (puzzle_input)

   return puzzle_input

def validateBirthYear(birthYear):
   isValid = True

   #Check length of birthYear
   if (len(birthYear) != 4):
      isValid = False

   if (int(birthYear) >= 1920 and int(birthYear) <= 2002):
      isValid = True
   else:
      isValid = False

   return isValid

def validateIssueYear(issueYear):
   isValid = True

   #Check length of issueYear 
   if (len(issueYear) != 4):
      isValid = False

   if (int(issueYear) >= 2010 and int(issueYear) <= 2020):
      isValid = True
   else:
      isValid = False

   return isValid

def validateExpirationYear(expYear):
   isValid = True

   #Check length of issueYear 
   if (len(expYear) != 4):
      isValid = False

   if (int(expYear) >= 2020 and int(expYear) <= 2030):
      isValid = True
   else:
      isValid = False
   return isValid

def validateHeight(height):
   isValid = True

   if "cm" in height:
      measurement = int(height.replace("cm", " "))
      if (measurement >= 150 and measurement <= 193):
         isValid = True
      else:
         isValid = False
   elif "in" in height:
      measurement = int(height.replace("in", " "))
      if (measurement >= 59 and measurement <= 76):
         isValid = True
      else:
         isValid = False
   else:
      isValid = False

   return isValid

def validateHairColour(hairColour):

   if re.match('^#[0-9a-z]{6}$', hairColour) != None:
      return True
   else:
      return False

def validateEyeColour(eyeColour):
   isValid = True

   if (eyeColour == "amb" or
       eyeColour == "blu" or
       eyeColour == "brn" or
       eyeColour == "gry" or
       eyeColour == "grn" or
       eyeColour == "hzl" or
       eyeColour == "oth"):
      isValid = True
   else:
      isValid = False

   return isValid

def validatePID(pid):

   if re.match('^[0-9]{9}$', pid) != None:
      return True
   else:
      return False

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
            passport = puzzle_input[x].replace("\n", " ")
            #print (passport)
            passportAttributes = passport.split(" ")
            #print (passportAttributes)
            #loop through passportAttributes, validating each
            validBirthYear = False
            validIssueYear = False
            validExpirationYear = False 
            validHeight = False
            validHairColour = False 
            validEyeColour = False 
            validPassportID = False 

            for i in range(0, len(passportAttributes)):
               keyValuePair = passportAttributes[i].split(":")
               #if valid key-value pair, do further processing
               if (len(keyValuePair) == 2):
                  if (keyValuePair[0] == "byr"):
                     validBirthYear = validateBirthYear(keyValuePair[1])
                  if (keyValuePair[0] == "iyr"):
                     validIssueYear = validateIssueYear(keyValuePair[1])
                  if (keyValuePair[0] == "eyr"):
                     validExpirationYear = validateExpirationYear(keyValuePair[1])
                  if (keyValuePair[0] == "hgt"):
                     validHeight = validateHeight(keyValuePair[1])
                  if (keyValuePair[0] == "hcl"):
                     validHairColour = validateHairColour(keyValuePair[1])
                  if (keyValuePair[0] == "ecl"):
                     validEyeColour = validateEyeColour(keyValuePair[1])
                  if (keyValuePair[0] == "pid"):
                     validPassportID = validatePID(keyValuePair[1])
            #print("Valid Birth Year: " + str(validBirthYear))
            #print("Valid Issue Year: " + str(validIssueYear))
            #print("Valid Expiration Year: " + str(validExpirationYear))
            #print("Valid Height: " + str(validHeight))
            #print("Valid Hair Colour: " + str(validHairColour))
            #print("Valid Eye Colour : " + str(validEyeColour))
            #print("Valid PID: " + str(validPassportID))
            #print("----------------------------")

            #Now check if all valid
            if (validBirthYear == True and
                validIssueYear == True and
                validExpirationYear == True and
                validHeight == True and
                validHairColour == True and
                validEyeColour == True and
                validPassportID == True):
                  count += 1



   return count

def main():
   puzzle_input = populate()

   validPassports = countValidPassports(puzzle_input)

   print ("Valid passports: " + str(validPassports))

if __name__ == "__main__":
   main()
