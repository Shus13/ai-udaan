# List : list built-in, mutable, ordered collection data type ho use to store multiple items in single variable

list_countries = ["nepal", "japan", "china", "bhutan"]

# List Operators : 
# Access item:
print(list_countries[0])

# Negative index
print(list_countries[-1])

# Slicing
print(list_countries[1:3])

# Check length
print(len(list_countries))

# List Methods
list_countries.append("argentina")
list_countries.insert(0,"canada")
list_countries.remove("canada")
list_countries.pop(4)
print(list_countries)



# Tuples : Yo chai ordered, unchangable collection ho which is use to store a fixed sequence of items, Duplicate allow hunxa

tuples_fruits = ("apple", "banana", "mango")

# Methods
print(tuples_fruits.count("apple"))
print(tuples_fruits.index("mango"))


# Sets : set chai unordered collection ho unique elements ko. Yo chia curly braces use gareyra define garinxa or set() function

sets_colors = {"red", "green", "yellow"}

# Methods
sets_colors.add("blue")
sets_colors.remove("blue")
sets_colors.pop()                   # clear is use to empty the set
print(sets_colors)

# We also have mathmatical methods like union, intersection difference
set_1 = {1, 3, 5, 0}
set_2 = {2, 4, 6, 0}

print(set_1.union(set_2))    
print(set_1.intersection(set_2))
print(set_1.difference(set_2))       



# Dictionary : Yo eauta built-in, mutable ani ordered collection ho jasley data key-value pair ma store garxa like object in js

profile_details = {
    "name" : "Sushit Karki",
    "address" : "Nepalgunj",
    "age" : 22,
    "campus" : "NCMT"
}

# Operations
# Access value
print(profile_details["age"])

# add/update
profile_details["height"] = "173cm"
print(profile_details)

# Methods
print(profile_details.get("name"))
print(profile_details.keys())
print(profile_details.values())
