'''
    Keyword ---> def
    Syntax  ---> def function-Name():
                    ## Body
    calling ---> function-Name()
'''

def First():
    print("Hello Mukesh!")
# ending function

print("Top")
First()     # Function is calling
print("Bottom")      # Top
                     # Hello Mukesh!
                     # Bottom

def mks(name):
    print("Hello " + name)
mks("mukesh")    # Hello mukesh
mks("Rakesh")    # Hello Rakesh

def mks(name,age):
    print("Hello " + name + ", You are "+ str(age))
mks("mukesh",23)    # Hello mukesh, You are 23
mks("rakesh",20)    # Hello rakesh, You are 20 

  # Using of 'Return' keyword 
def cube(num):
    return num*num*num
print(cube(3))   # 27

def cube(num):
    return num*num*num
result = cube(3) 
print(result)   # 27

def cube(num):
    return num*num*num
    print("Code")   # don't print code b/z 'return' is used like 'break' keyword
result = cube(3) 
print(result)   # 27

