#RandomNumGuessingGame
#creates an array with a user specified number of random numbers between 1 and 100
#player has a random number of tries to guess al the numbers in the array

import random   
from random import randint
def randomNumGen(size, data=[]):
   randNum = randint(0,size)
   if data:
        while randNum in data:
            randNum = randint(0,size)
        return(randNum)

def GetRandDatabase(size):
    RandDatabase=[randomNumGen(size)]
    print("Generating"+ " " + str(size) + " " + "random integers between 1 and 100...")
    for a in range(size):
        RandDatabase.append((randomNumGen(100, RandDatabase)))
    print("Done generating random integers!")
    RandDatabase=RandDatabase[1:]
    return RandDatabase
    
def ShowDatabase(size, RandDatabase):
    print ("The integers in this database are:")
    for a in range(size):
        print ("Integer", [a], "=", RandDatabase[a])
    
def SearchDatabase(RandDatabase, GivenNumber):       
   if int(GivenNumber) in RandDatabase:
        this = True
   else:
        this = False
   if this == True:
        print("Good job! You Found " + str(GivenNumber) + " in " + str(TriesTaken+1) + " attempts.")
   elif this == False:
        print ("Ooops " + str(GivenNumber) + " is not in my database.")      

def GuessGame(size):
    RandDatabase=GetRandDatabase(size)
    TriesRemaining=random.randint(1,size)
    global TriesTaken
    TriesTaken=0
    while TriesRemaining>=1:
        GivenNumber=input("Please enter integer to search for:")
        SearchDatabase(RandDatabase, GivenNumber)
        TriesRemaining -=1
        TriesTaken+=1
    print ("You are out of tries! Game Over :(")
    ShowDatabase(size,RandDatabase)
    Again=input("Would you like to play again? {Yes or No}:")
    if Again == "No":
        print ("Goodbye")
    if Again == "Yes":
        GuessGame(size)
                   
    
