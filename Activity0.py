set1 = set("abcdklmij")
set2 = set("efghnopdij")
set3 = set("qrstklmnopij")

def iandj():
    print(set1.intersection(set2, set3))
iandj()

def abc():
    print(set1.difference(set2,set3))
abc()

def ijnop(): 
    print(set2.intersection(set3))
ijnop()

def d():
    print(set1.intersection(set2).difference(set3))
d()

def klmnop(): 
    set4 = set1.intersection(set3).difference(set2)
    set5 = set2.intersection(set3).difference(set1)
    set6 = set4.union(set5)
    print(set6)
klmnop()
