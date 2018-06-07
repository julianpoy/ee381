import math

numbers = []

while True:
  try:
    n = int(input("Enter a natural number. Enter a letter to stop: "))
    numbers.append(n)
  except ValueError:
    break
numbers.sort()

def my_mean(input_list):
  return sum(input_list) / len(input_list)

def my_median(input_list):
  median = -1
  if len(input_list) % 2 == 0:
    first = int(len(input_list) / 2) -1
    last = int(len(input_list) / 2)
    return (input_list[first] + input_list[last]) / 2
  else:
    return input_list[int(len(input_list) / 2)]

def my_mode(input_list):
  from collections import Counter
  
  c = Counter(input_list)
  
  mode = c.most_common(1)
  
  return mode[0][0]

def my_deviation(input_list):
  y = 0
  a = 0
  for x in input_list:
    y = (x - my_mean(input_list))**2
    a = a + y
  return math.sqrt(a / len(input_list))

print("Mean is: ", my_mean(numbers))
print("Median is: ", my_median(numbers))
print("The mode is: ", my_mode(numbers))
print("The standard deviation is: ", my_deviation(numbers))

# I separated this problem into many helper functions that are reusable
# At work, we prefer to write functions this way for maintainability. I hope you don't mind
