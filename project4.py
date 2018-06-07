# Simulate a binomial distribution
# The binomial distribution viewed as a sum of bernoulli trials.
# Simluate the following problem
# n = 5, the number of trials
# p = 0.7, the problem of success for any one outcome
# x = 3, the number of successes

import random

n = 18
p = 0.5

xCoords = list(range(0, 18)) # Desired x (success) values track
jStats = [0] * len(xCoords) # Accumulator variable

# Number of repitions
N = 100000

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

jStats = [ x / N for x in jStats ] # Convert to probability

desiredCVFit = 0.05

distance = [ abs(x - desiredCVFit) for x in jStats ]

bestCV = xCoords[distance.index(min(distance))]

print("Part 1 ----")
print("Closest CV: ", bestCV)
print(xCoords)
print(jStats)
import matplotlib.pyplot as plt

plt.bar(xCoords, jStats)

plt.show()

# Type 2 -----

pVals = [i / 100 for i in range(55,101) if i % 5 == 0] # Range between 0.55 - 1.00 in increments of 5

j = [0] * len(pVals) # Accumulator variable

trial = [0] * n

for k in range(N):
  
  for p in pVals:
    for i in range(n): # Inner loop - the trials
      
      # Below are the Bernoulli trials
      r = random.uniform(0,1)
      
    
      if r < p:
        trial[i] = 1
      else:
        trial[i] = 0
    
    s = sum(trial)
      
    if s == bestCV:
      j[pVals.index(p)] += 1

print(j)

print("Part 1 ----")
print("Closest CV: ", bestCV)
print(pVals)
print(j)

plt.bar(pVals, j)

plt.show()
