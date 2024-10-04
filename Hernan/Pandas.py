import pandas as pd
###################################################
############Dictionary to DataFrame################
###################################################

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names
          ,'drives_right': dr
          ,'cars_per_cap': cpc
          }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

######################################################
#################CSV to DataFrame#####################
######################################################

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\Users\User\Documents\REPOSITORY\DataSciencesWithPython\Files\Input\cars.csv')

# Print out cars
print(cars)

# Fix import by including index_col
cars = pd.read_csv(r'C:\Users\User\Documents\REPOSITORY\DataSciencesWithPython\Files\Input\cars.csv', index_col = 0)

# Print out cars
print(cars)