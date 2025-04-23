#question 1:
set1 = set("abcdefg")
set2 = set("adegjke")
set3 = set("aaaaaaaaa")

print(set1) 
print(set2)
print(set3)

#Qustion 2:
#are sets mutable? yes sets are mutabled 
#are sets ordered? no sets are unordered
#are sets iterable? yes sets are iterable
#Can I determine the length of a set? yes we can determine the length of a set using len() function
#can i determine if a specific element is in a set? yes we can determine if a specific element is in a set using 'in' operator

#question 3:
d = {} #empty dictionary 
s = set() #empty set
print(d)
print(s)

#-Whatisit1 = dictionary because it has a key value pair 
#-Whatisit2 = set because it has no key value pair just "Bob"

#question 4:
#set1.pop() #pops a random element from the set
#print(set1)
#set1.add("h") #adds an element to the set in a random position
#print(set1)
#set2.remove("a")
#print(set2) #removes an element from the set

#question 5:
print(set1.intersection(set2))#returns the common elements in both sets
print(set1.union(set2))#returns all the elements in both sets
print(set1.difference(set2))#returns the elements in set1 that are not in set2
print(set1.symmetric_difference(set2))#returns the elements that are in set1 or set2 but not in both

set4 = set1.symmetric_difference(set2)
print(set4.isdisjoint(set2))#returns true if the sets have no elements in common
print(set4.isdisjoint(set3))#returns true if the sets have no elements in common