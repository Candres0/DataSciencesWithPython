#Dictionary to DataFrame
import pandas as pd
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict={"country":names, "drives_right":dr, "car_per_cap":cpc}
cars = pd.DataFrame(my_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels
# Print cars again
print(cars)


#CSV to DataFrame
cars = pd.read_csv('/Users/andrescampino/Reposiroties/DataSciencesWithPython/Files/Input/cars.csv')
print(cars)

#Change index_col
cars = pd.read_csv('/Users/andrescampino/Reposiroties/DataSciencesWithPython/Files/Input/cars.csv', index_col = 0)
print(cars)