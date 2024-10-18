import numpy as np

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))


house = [["hallway", 11.25], 
        ["kitchen", 18.0], 
        ["living room", 20.0], 
        ["bedroom", 10.75], 
        ["bathroom", 9.50]]

# Build a for loop from scratch
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
        'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)


np_baseball = np.array([[74, 180],[74, 215],[72, 210],[75, 205],[75, 190],[73, 195]])
np_height = [74, 74, 72, 75, 75, 73]
# For loop over np_height
for x in np_height:
    print(str(x) + " inches")
# For loop over np_baseball
print(np_baseball)
for x in np.nditer(np_baseball):
    print(str(x))