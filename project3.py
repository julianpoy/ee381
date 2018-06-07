# Simulate a binomial distribution
# The binomial distribution viewed as a sum of bernoulli trials.
# Simluate the following problem
# n = 5, the number of trials
# p = 0.7, the problem of success for any one outcome
# x = 3, the number of successes

import random

n = int(input('Enter the number of trials: '))
p = float(input('Enter the probability of success: '))
x1 = int(input('Enter the number of successes desired (starting, inclusive): '))
x2 = int(input('Enter the number of successes desired (ending, inclusive): '))

xCoords = list(range(x1, x2)) # Desired x (success) values track
jStats = [0] * len(xCoords) # Accumulator variable

# Number of repitions
N = int(input('Enter the number of repetitions (best to choose a value less than 100000): '))

trial = [0] # Single entry in Python list.
trial = trial * n # List of size n filled with zeros

E = 0 # Accumulator for average

for k in range(N):
  
  for i in range(n): # Inner loop - the trials
    
    # Below are the Bernoulli trials
    r = random.uniform(0,1)
    
    if r < p:
      trial[i] = 1
    else:
      trial[i] = 0
  
  # print(trial)    
  s = sum(trial)
    
  E = E + s
    
  if s in xCoords:
    jStats[xCoords.index(s)] += 1

prob = jStats[0] / N # Number of desired successes relative to the total number of repetitions

ave = E/N

print("Parts 1 and 2 ----")
print("The probability for index 0 of the range you specified is ", prob)
print("The expected (average) value is ", ave)

print("Part 3 ----")
import matplotlib.pyplot as plt

plt.bar(xCoords, jStats)

plt.show()
