# Import numpy as np
import numpy as np
# Set the seed
np.random.seed(123)
# Generate and print random float
print(np.random.rand())

#Throw the dice
# Use randint() to simulate a dice
print(np.random.randint(1, 7))
# Use randint() again
print(np.random.randint(1, 7))

'''you're walking up the empire state building to DataCamp HeadQuarters and you're playing a game with a friend.
You throw a die.
If it's 1 or 2 you'll go one step down.
If it's 3, 4, or 5, you'll go one step up.
If you throw a 6, you'll throw the die again and will walk up the resulting number of steps.'''
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

if dice <= 2 :
    step = step - 1
elif dice >= 3 and dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
