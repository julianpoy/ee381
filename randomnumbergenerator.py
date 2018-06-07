M = 8601
A = 4857
N = 10000

S = int(input('Enter your seed: '))

k = int(input('Enter the number of random numbers you want: '))

counter = 0

for i in range(1, k+1):
    S = (M*S + A) % N
    
    r = S / N
    
    counter += r
    
    print(format(r, '.4f'))

print("Mean is: ", counter / k)

# When at its best, this should generate a mean of 0.5
# Of course, we will rarely see exactly that.
