## IGNORE THIS SECTION

import re


file = open("hamlet.txt","r")

def count(term):
  result = re.findall(term, file.read())
  if result:
    result = len(result)
  else:
    result = 0 
  print("Occurrences of '" + term + "': " + str(result) + "\n")
  file.seek(0)  # reset file to beginning

def find(term):
  print( "Lines with '" + term + "':")
  count = 1
  for line in file:  
    if line.find(term) > -1:
      print( str(count) + ": " + line )
    count += 1
  print("")
  file.seek(0)  # reset file to beginning




## START HERE!

## count the number of occurrences of a word or phrase
# searchTerm = 'Hamlet'
# count( searchTerm)

## find all the lines that contain a word or phrase
# find( "Queen." )

count('Ophelia.')
