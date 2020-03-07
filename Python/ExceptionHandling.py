try:
    number = int(input("Enter a number : "))
    print(number)

except:
    print("invalid Input")   # mks   ---> invalid input

#Divide by Zero Problem 

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("invalid input")     # division by zero
