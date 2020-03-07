#Create a variable
string1 = "Mukesh"
print(string1)

# To change a line
print("mukesh \n kumar")

#Change all fonts into Lower case
print(string1.lower()) # mukesh

#Change all fonts into Upper case
print(string1.upper()) #MUKESH

# to check Letters is upper or not
print(string1.upper().isupper())  # True

print(string1.isupper())  # False


# Find the length of the string
print(len(string1))  # 6

# Accessing letters one by one
print(string1[0])  #  M

print(string1[1])  # u

print(string1[2])  # k

#Accessing index one by one

print(string1.index("M"))  # 0

print(string1.index("k"))   # 2

print(string1.index("es"))  # 3

# Replace the word
print(string1.replace("esh","Rakesh"))  # MukRakesh
print(string1) # Mukesh