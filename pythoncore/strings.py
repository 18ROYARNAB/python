# STRINGS ARE IMMUTABLE 
str1="my name is Roy"
str2='Coding'
str3="""God's child """ #triple quotation to use 's in string

# STRING SLICING
print(f"here is {str2[1:6]}")
print(f"here is {str2[1:]}")
print(f"here is {str2[:]}")
print(f"here is {str2[:-1]}")
print(f"here is {str2[1:len(str2)]}")

# STRING FUNCTIONS
str1.endswith("oy") # returns true if string ends with substr
str1.capitalize(str1) # capitalize 1st letter
str1.replace("my","you") #replaces all occurence with new
str1.find("Roy")# returns the index where substr is found at first
str1.count("m") # returns the total count of substr occurence.

