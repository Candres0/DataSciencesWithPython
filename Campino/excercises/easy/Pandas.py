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

##########Square brackets##########

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

########loc and iloc#########

# Print out observation for Japan
print(cars.loc['JPN'])
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1,-1]])

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])
print(cars.iloc[-2,2])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])
print(cars.iloc[[4,-2],[1,2]])

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
print(cars.iloc[:, [0,2]])
