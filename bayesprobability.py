# Calculate bayes probability
# C = 0.0001, P(C), the probability of having the disease
# B = 0.9, P(B|C), the probability of a positive test result given that you have the disease
# Bnot = 0.001, P(B|C'), the probability of a positive test result given that you do not have the disease

import random
C = [0.0001, 0.001, 0.001, 0.0001, 0.001]
Cnot = [1-x for x in C]
B = [0.9, 0.9, 0.9, 0.95, 0.95]
Bnot = [0.001, 0.001, 0.01, 0.001, 0.01]

results = []
for i in range(len(C)):
  result = (C[i]*B[i])/((C[i]*B[i]) + (Cnot[i]*Bnot[i]))
  results.append(result)

print(results)
