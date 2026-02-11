import numpy as np

# Number of times to roll the dice
rolls = 100

# Simulate dice rolls (1 to 6)
dice = np.random.randint(1, 7, rolls)

print("Dice Rolls:\n", dice)

# Count frequency of each number
for i in range(1, 7):
    count = np.sum(dice == i)
    print(f"Number {i} occurred {count} times")

