# now this is a comment
"""
this is a block comment
"""
print "hello world"

var_name = 1

#string
s = "this is a string"
print s

#numbers
a = 7 #int
b = 3
c = 3.2 #float

print float(a)/b # will print with accuracy now vs roundng error

print 2^2 #wont work for raising to a power
print 2**2 # works! 2 to the power of 2

import math
print math.floor(8.3) #drops it to the lowest float of that int
print math.floor(9.1)

#boolean
x = True
y = False

a = 89
print a == 89
print not(a == 89)

#conditionals
x = input("Enter a number: ")
y = int(raw_input("enter an int: "))
print x
print y

#colons signify the next line should be indented
if y % 2 == 0:
    print y, "is an even number"
else:
    print str(y) + "is an odd number"

#lists
empty_list = []
non_empty_list = [1,2,3,4]
print non_empty_list

mixed_type_list = [1,2,3.0,'string',True]
embedded_list = [ [], [], 112]
print non_empty_list[0] #prints first element in array
print non_empty_list[-2] #prints the second to LAST element in array
print non_empty_list[-1] #prints the LAST element in the array

print len(non_empty_list) #prints list length

non_empty_list[0] = 999
non_empty_list.append([1,2,3]) #will imbed this list into the other list
print non_empty_list

non_empty_list.remove(999) #will remove first element of that value
non_empty_list.pop(2) #removes element at index 2
non_empty_list.extend([8,9,10]) #adds these numbers to the list as individual elements

#slicing
print non_empty_list[2:5] #prints index 2 through 4 (ie EXCLUDES 5)
print non_empty_list[1:] #prints everything thorugh end from the intital index

some_list = ["derp", 33, 45]
list_copy = some_list[:]

#sets
a = set([1,2,3,4]) #a set CANNOT REPEAT VALUES
print a
b = set([1,1,2,4,5,4])  #will print out only 4 values (1,2,4,5) and just DOESNT PRINT REPEATS
print 1 in b #will print true if one is in b
print a.intersection(b)
print a.union(b)

print a - b #prints complement (ie the elements that are in a that arent in b
print a | b #union puts both sets together
print a & b #intersection
print a ^ b #elements in a or b but NOT in both

#tuples (are immutable)
some_tuple = (1,2,3)
#some_tuple[0] = 88 CAUSES ERRROR  cant change any of it

#functions
def some_function(some_input):
    pass

def print_if_large(some_str):
    """
    print if the length of the given string is greater than 10
    """
    if len(some_str) > 10:
        print "length of string is large"
    else:
        print "length of string is not large"

print print_if_large('this is one really long string')

def is_large(some_str):
    """
    determines if string is large and returns boolean
    """
    return len(some_str) > 10

print is_large("small")

def cut_large_string(some_str):
    #cuts a string over length 10 to length 10
    if is_large(some_str):
        return some_str[:10]
    return some_str

print cut_large_string("hola me llamo maria casciani")




