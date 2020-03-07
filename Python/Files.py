# Create a new file
employee = open("employee.txt","w")  # create a file

employee.write("Rakesh Kumar")   # write on file

employee.close()         # close the file


employee_file = open("employee.txt","r")  # "r" for reading mode

print(employee_file.readable())   # gives boolean result

print(employee_file.read())  # read the content of file

print(employee_file.readline())   # read the first line of the file

employee_file.close()   # close the file

# o/p ---> True

# For Loop in the file
employee_file = open("employee.txt","r") 
for emp in employee_file.readlines:
    print(emp)
employee_file.close()


# Writing to Files
employee_file = open("employee.txt","a")  # "a" means at the end
employee_file.write("You are a smart guy! ")
employee_file.close()

# if you replace "a" with "a" ,  then it override the file i.e. it deletes all the content of old file.

