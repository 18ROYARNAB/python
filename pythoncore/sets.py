# SET IS DATA STRUCTURE IN WHICH IS MUTABLE BUT ONLY STORES IMMUTABLE ELMENTS LIKE STR,BOOL,PRMITIVE DATATYPES,TUPLE ARE STORED NO LIST OR DICTIONARY CAN BE STORED IN SET AND REPEATED ELEMENTS ARE DISPLAYED ONCE ONLY 
collection={1,2,2,4,5,"hello","World","World",4}

print(collection)
print(type(collection)) # empty set
NULL_set=set()

# methods in set
collection=set()
collection.add(3)
collection.remove(3)
collection.pop()
collection.clear() #empties set
collection.union(set2)#sets union as in math
collection.intersection(set2)#sets intersection as in math
print(collection)