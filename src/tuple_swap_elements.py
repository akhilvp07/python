list1 = [(2,3),(7,5),(6,7),(8,9),(7,11)]

print("The original list is :" + str(list1))

res = [(sub[1], sub[0]) for sub in list1]

print("The swapped tuple list is :" + str(res))