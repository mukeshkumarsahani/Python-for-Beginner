# It contains different values similar to list but you can't change values if once a tuple is created.

coordinate = (4,5)
print(coordinate[0])  #4

print(type(coordinate))   # <class 'tuple'>

coordinate[1] = 10  # TypeError: 'tuple' object does not support item assignment
print(coordinate)   # (4, 5)

