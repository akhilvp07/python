num = 7
list1 = [(2,3),(7,5),(6,7),(8,9),(7,11)]

output = [item for item in list1
          if item[0] == num or item[1] == num]
print(output)