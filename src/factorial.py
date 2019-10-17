import sys

count = int(len(sys.argv))
if(count != 2):
    print("Usage: {0} <num>".format(sys.argv[0]))
    exit(-1)
    
num = int(sys.argv[1])
fact = 1
for i in range(1, num+1):
    fact=fact*i

print("Factorial of {0} is {1}".format(num, fact))