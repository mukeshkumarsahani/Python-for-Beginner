is_male = True   # create a boolean variable
if is_male:     
    print("You are a male")    # You are a male

is_male = False   # create a boolean variable
if is_male:     
    print("You are a male")   # Nothing to show

# If ---Else statement

is_male = False
if is_male:
    print("You are male.")
else:
    print("You are not a male.")  # You are not a male.

is_male = True
if is_male:
    print("You are male.")
else:
    print("You are not a male.")  # You are male.

# if---or----else statement

is_male = True
is_tall = False
if is_male or is_tall :  # if one condition is true,the code is executed
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = False
is_tall = False
if is_male or is_tall :
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# if---and----else statement


is_male = True
is_tall = True
if is_male and is_tall :  # if both conditions are true,the code is executed
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


is_male = True
is_tall = False
if is_male and is_tall :  
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# elif ----- and not, elif not ----- and  statements 

is_male = True
is_tall = False
if is_male and is_tall :  
    print("You are a male or tall or both")
elif is_male and not is_tall:
    print("You are short male")
elif not is_male and is_tall:
    print("You are not a male but tall")
else:
    print("You are neither male nor tall")    # o/p -->  You are short male

# if statements with comparisons

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))    # 5

# CALCULATOR

num1 = float(input("Enter 1st number: "))
op = input("Enter operator: ")
num2 = float(input("Enter 2nd number: "))

if op == "+" :
    print(num1 + num2)
elif op == "-" :
    print(num1 - num2)
elif op == "*" :
    print(num1 * num2)
elif op == "/" :
    print(num1 / num2)
else:
    print("Please enter a valid operator within +,-,* and /")   
                                                                 
# while loop

i = 1
while i <= 10:
    print(i)
    i= i+1
print("Done")

# Building a guessing Game

secret_word = "giraffe"
guess = ""
while guess != secret_word :
    guess = input("Enter guess : ")
print("You win")


secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess : ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("Out of guesses, YOU LOSE !")
            
print("You win !")

# For loop 

for letter in "Mukesh" :
    print(letter)

friends = ["abhishek", "Chandan", "Jaspreet"]
for friend in friends:
    print(friend)

for i in range(10):
    print(i)

for i in range(3,10):
    print(i)

for i in range(len(friends)):
    print(i)

for i in range(len(friends)):
    print(friends[i])

# Exponent Function

print(2**3)   # 8

def raise_to_power(base_num, power_num):
    result = 1
    for i in range(power_num):
        result = result * base_num
    return result
print(raise_to_power(4,3))        # 64

