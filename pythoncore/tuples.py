# TUPLES ALLOWS TO STORE IMMUTABLE SEQUENCE OF DATA THAT IS LISTS BUT IMMUTABLE

tup=(1,5,32,2,34)
print(tup[0])
print(tup[2])

# assigning value is not allowed 
# tup[0]=4

# SLICING TUPLES
print(tup[1:])
tup[:3]

#TUPLE METHODS
print(tup.index(5)) # returns 1st occurence  index of the element
print(tup.count(2)) # returns count of the element

# INPUT FROM USER USING LOOPS