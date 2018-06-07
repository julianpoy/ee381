M = 8601
A = 4857
N = 10000

S = int(input('Enter your seed: '))

def get_random():
  global S
  S = (M*S + A) % N
  r = S / N
  return r
  
trial_count = 10000000
separate_bucket_count = 0

for x in range(trial_count):
  
  cups = [0]*5 # All cups begin empty (0)

  # Sort balls
  for i in range(5):
    bucket = int(get_random() * 5)
    
    cups[bucket] += 1 # Bucket that ball landed in gets incremented
    
  all_separate_buckets = True # Presume true
  for i in range(5):
    if cups[i] != 1:
      all_separate_buckets = False
      break
    
  if all_separate_buckets:
    separate_bucket_count += 1
      
print("Probability is: ", separate_bucket_count / trial_count)
    

# This problem can be solved on paper as such:
# n!/(n-k)!n^k
# Number of cups (n) => 5
# Number of balls (k) => 3
# Answer is 0.48

# Another way to think about this is
# As the balls are thrown, this is the probability:
# (1) * (4/5) * (3/5)
# As the cups fill up, the open cups decrease
# Same result, 0.48
    


