import sys

count = int(len(sys.argv))
if(count != 2):
    print("Usage: {0} <num>".format(sys.argv[0]))
    exit(-1)

num = int(sys.argv[1])
result = 0
while num != 0:
    result = result +int(num%10)
    num=int(num/10)

print("Sum of digits of {0} is {1}".format(int(sys.argv[1]), result))
