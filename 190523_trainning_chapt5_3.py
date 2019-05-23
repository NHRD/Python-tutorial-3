sam = ["  a", "b", "c  "]
new = [weapon.strip() for weapon in sam]
print(new)

tap = [(x, x**2) for x in range(6)]
print(tap)

lis = [[x, x**2] for x in range(6)]
print(lis)

lisn = [[row[i] for row in lis] for i in range(1)]
print(lisn)

lisnn = list(zip(*lis))
print(lisnn)

del lisnn[0]
print(lisnn.pop(0))
print(lisnn)
