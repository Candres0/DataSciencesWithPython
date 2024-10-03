 import math as mth
from math import pi

# Addittion
print(5+4)

#Rest
print(5-5)

#Multiplication
print(3*5)

# Division(Comentario)
print(7/2)


#create variable
savings = 100

print(savings)

#excersise
monthly_savings = 10
num_months = 4
total_savings = monthly_savings*num_months

print(total_savings)

#float
half = 0.5
intro = "hello, how are you?"
is_good = True

print(half)
print(intro)
print(is_good)

#Diferent Types
x = type(total_savings)

print(x)

#concant
double_intro = intro + intro

print(double_intro)

#list
hall = 20
kit = 10
liv = 30
bed = 50
bath = 60

areas=["hallway",hall,"kitchen",kit,"living-room",liv,"bedroom",bed,"bathroom",bath]

print(areas)

#list of list

hall = 20
kit = 10
liv = 30
bed = 50
bath = 60

areas = [["hallway",hall],["kitchen",kit],["living-room",liv],["bedroom",bed],["bathroom",bath]]

print(areas)

#indexing of list
areas = ["hallway",hall,"kitchen",kit,"living-room",liv,"bedroom",bed,"bathroom",bath]

print(areas[1])
print(areas[9])
print(areas[-1])
print(areas[5])

#slicing
downstairs = areas[0:6]
upstairs = areas[6:]

print(downstairs)
print(upstairs)

home = [["hallway", 11.25],
        ["kitchen", 21.54],
        ["living-room", 34.87],
        ["bedroom", 12.7],
        ["bathroom", 9.5]]

print(home[-1][1])

#modifying list
areas = ["hallway",11.25,"kitchen",21.54,"living-room",34.87,"bedroom",12.7,"bathroom",9.5]

areas[-1]= 11.6

areas[4]= "chill zone"

print(areas)

areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage", 34.6]

print(areas_2)

del areas_2 [10]
del areas_2 [10]

print(areas_2)

areas_copy = list(areas)

areas_copy[0] = 12.8

print(areas_copy)
print(areas)

#function

var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

#function documetary
#?out2 

first=(11.25,18.3,23.6)
second=(13.75,9.56)

#help(sorted)

full = first + second
full_sorted = sorted(full,reverse=True)

print(full_sorted)

#methods
place = "poolhouse"

place_up = place.upper()

print(place_up)

print(place.count('o'))

areas_t = [11.3,34.5,12.4,56.7,30.6]

print(areas_t.index(12.4))

print(areas_t.count(56.7))

areas_t.append(21.6)
areas_t.append(15.8)

print(areas_t)

areas_t.reverse()

print(areas_t)

# circumference of the circle

c = 2 * 0.43 * mth.pi

# area of the circle (import all package)

a = mth.pi * 0.43 **2 

print("circumference:" + str(c))
print("area:" + str(a))

#(selective import)
c = 2 * 0.43 * pi

a = pi * 0.43 **2

print("circumference:" + str(c))
print("area:" + str(a))


