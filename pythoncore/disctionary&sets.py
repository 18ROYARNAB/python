# STORS DATA IN KEY VALUE PAIRS / mutable and unordered and duplicate keys not allowed key can be any data type
dict1 = {
    "nsmr":"arnab",
    "age":21,
    "friends": ["roy","rishv","risser"],
}
print(dict1)

# accessing data from disctionary

print(dict1["age"])

# inserting new key val pair

dict1["surname"]="roy"
print (dict1)

#updating existing values by keys

dict1["age"]=99
print (dict1)

#nwsted dictionary

students={
    "name": "arnab",
    "subject":{"phy":50,"chem":45, "math":49,
    },
}
# accessingnested dictionary

print(students["subject"]["math"])

#Mehthods dictionary
print(students.keys()) # gives all keys in the dictionary
print(students.values())# gives all the values 
print(students.items())# gives all key value pairs 

print(students.get("name")) # gives value for a particular key 

new_dict={"city":"askr"}
students.update(new_dict)
print(students)