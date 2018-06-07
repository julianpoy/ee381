import random

probability = 0.659

trial_count = 10000

sample_size = 500
sums = [0] * sample_size

successes = 0

for i in range(trial_count):

  for j in range(sample_size):
    r = random.uniform(0,1)

    if r < 0.659:
      sums[j] = 1
    else:
      sums[j] = 0
      
  total = sum(sums)
  
  if total == 340:
    successes += 1
    
probability_result = successes / trial_count

print("Total is: ", probability_result)
  