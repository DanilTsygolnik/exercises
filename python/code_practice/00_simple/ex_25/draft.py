# how to use enumerate instead range(0, len(list))
for i in [5,6,7,8]:
    print(i)
for i, _ in enumerate([5,6,7,8]):
    print(i)

