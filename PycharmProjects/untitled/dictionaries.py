#dictionaries ~ hashmaps in python
dictionary_name = {} #empty dictionary
book = dict(page1="title", page2="blank page")
print book
book2 = dict.fromkeys([1,2,3], "one") #intializes values to "one", can only be one value
print book2

#how to change values
book2[2] = "two"

#how to add values
book2[5] = "five"
print book2

#in keyword allows you to check if a certain key exists
print 1 in book2 #prints True
print "1" in book2 #prints False (TYPE MATTERS))

#how to check values
print 'one' in book2.values()  #prints true

#prints all the keys
print book2.keys()

#prints all the keys
print book2.values()

#how to combine dictionaries
print book2.update(book)

#nested structures (dictionaries in dictionaries)
nest = {1 : {2:{3:"nested!"}}}
print nest[1][2][3] #prints the value stored at this very nested location

#while loops
num = 0
while num < 3:
    print num
    num += 1

items = ["a" , 'b' , 'c']
ind = 0
while ind < len(items):
    print items[ind]
    ind+=1

#for loops
for _ in range(2,5): #and _ is ok to use; signifies when the values being iterated through dont matter
    print _         #prints 2--> 4

for _ in range(2,5,2):
    print _             #prints 2 and 4

#pass --> useful as a placeholder when laying out program structure
#would put pass say in a fxn body that you haven't filled yet

#list comprehensions --> basically for when you append things to a list
#[VALUE for ITEM in CONTAINER if CONDITION]
even_squares = [num ** 2 for num in range(0,11) if num%2 == 0]

a = range(6) #autimatically makes a list of 0 - 5
b = [11, 22, 33, 44, 55, 66]

numbers = {}
numbers.fromkeys(a, 1)
for i in range(len(a)):
    print i
    numbers[i] = b[i]
print numbers.keys()
print numbers.values()

values = {a[i] : b[i] for i in range(len(a))} #uses list comprehension to fill a dictionary  with the desired values
print values

#zipping
c = ['hi','hello','bye']
d = [3,4,5]
print zip(c,d)

v = list(range(2,10,2))
l = list(range(2,10,4))
def merge(list1,list2):
    x = set(list1)
    y = set(list2)
    j = x & y
    return list(j)
print merge(v,l)

def merge2(list1,list2):
    return list(set(list1) & set(list2))
print merge2(v,l)



