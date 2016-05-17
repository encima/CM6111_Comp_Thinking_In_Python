from time import time
from random import shuffle

n = 10    #Number of items in the list
myList = []

#This function creates the list of size n
for num in range(n):
   myList.append(num)

#shuffle(myList)    #Randomly shuffle the order of myList
#myList.reverse()   #myList is put in reverse order

print 'Original List', myList
pos = 0    #Which position are you in the list
step = 0   #Keep track of the number of steps to complete the sort
start = 0  #Initialize the start time

start = time()    #Get the start time
while (pos < len(myList) - 1):    #Pseudocode line 4
   if myList[pos] > myList[pos + 1]:    #Pseudocode line 2
      myList[pos], myList[pos + 1] = myList[pos + 1], myList[pos] #Swap
      pos = 0    #Pseudocode line 2a
   else:
      pos += 1    #Pseudocode line 3
   step += 1

print 'Sorted List', myList
print 'Steps used:', step
print 'Total time:', time() - start    #Print out the time elapsed
