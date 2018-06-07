# Simulate a binomial distribution
# The binomial distribution viewed as a sum of bernoulli trials.
# Simluate the following problem
# n = 5, the number of trials
# p = 0.7, the problem of success for any one outcome
# x = 3, the number of successes

import random
n = 5
p = 0.7
x = 3

# Number of repitions
N = 1000000

trial = [0] # Single entry in Python list.
trial = trial * n # List of size n filled with zeros

j = 0 # Accumulator variable initialized

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
    
  if s == x:
    j = j + 1

prob = j / N # Number of desired successes relative to the total number of repetitions
print(prob)
