marks = [23.3,54.6,78.7,56.0,65.9]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

# STRING ARE IMMUTABLE LISTS ARE MUTABLE
marks[0]= 10
print(marks)
# str='hello'
# str[0]='y'
# print(str)

# slicing in list 
print(marks[:len(marks)])
print(marks[1:4])
print(marks[:-1])
print(marks[1:len(marks):2])

# METHODS IN LISTS

marks.append(4) # adds an element at last index
marks.sort()# arranges in ascending order 
marks.sort(reverse=True) # arranges in descending order
marks.reverse()# reverses a list
marks.insert(1,10) # inserts 10 at index 1
marks.remove(1)# removes the 1st occurence of element
marks.pop(2)# removes element from a index

# INPUT FROM USER USING LOOPS
list_movies=[]
for i in range (3): 
    movie=input("Enter your favourite movies")
    list_movies.append(movie)

print(list_movies)
print(type(list_movies))