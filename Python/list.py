# A list can store different datatype within it. And it further can modified easily.

varlist = ['pradeep','akash','rakesh','jaspret','mukesh']

# Print the first element
print(varlist[0])  # pradeep

# print the last element of the list
print(varlist[-1])  # mukesh

print(varlist[1:])   # ['akash', 'rakesh', 'jaspret', 'mukesh']

print(varlist[1:4])   # ['akash', 'rakesh', 'jaspret']

# Replace the specific value
varlist[1] = "Abhishek"
print(varlist)    # ['pradeep', 'Abhishek', 'rakesh', 'jaspret', 'mukesh']

numbers = [14,8,15,16,23,42]
friends = ["AA","BB","CC"]
print(friends)   ##  ["AA","BB","CC"]

# Add at last of the list
friends.append("Mukesh")
print(friends)   #  ['AA', 'BB', 'CC', 'Mukesh']

# Add two lists
friends.extend(numbers)
print(friends)      # ['AA', 'BB', 'CC', 'Mukesh', 14, 8, 15, 16, 23, 42]

# Check datatype
print(type(friends))   # <class 'list'>

# Insert value at any place 
friends.insert(1,"Rakesh")
print(friends)             # ['AA', 'Rakesh', 'BB', 'CC', 'Mukesh', 14, 8, 15, 16, 23, 42]

# Remove any values from list
friends.remove("CC")
print(friends)        # ['AA', 'Rakesh', 'BB', 'Mukesh', 14, 8, 15, 16, 23, 42]

# Clear the list
numbers.clear()
print(numbers)    # [] an empty list

# Delete top element of the list
friends.pop()
print(friends)    # ['AA', 'Rakesh', 'BB', 'Mukesh', 14, 8, 15, 16, 23]

# Find the index position of values in the list
print(friends.index("Mukesh"))   # 3

# Count the total repeated values one by one
print(friends.count("Mukesh"))  # 1

# Sorting of list
num2 = [4,67,23,567,34,2,76,8,45]
num2.sort()
print(num2)   # [2, 4, 8, 23, 34, 45, 67, 76, 567]

# print(num2.sort())  --> None
# print(friends.sort())   --> can't be sort b/z it has different datatypes

Strlist = ['mks','rks','akp','jp']
Strlist.sort()
print(Strlist)   # ['akp', 'jp', 'mks', 'rks']

# Reverse the list
num2.reverse()
print(num2)    # [567, 76, 67, 45, 34, 23, 8, 4, 2]

# Copy the list into the another list
strlist2 = Strlist.copy()
print(strlist2)    # ['akp', 'jp', 'mks', 'rks']

