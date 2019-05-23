sam = ["  a", "b", "c  "]
new = [weapon.strip() for weapon in sam]
print(new)

tap = [(x, x**2) for x in range(6)]
print(tap)

lis = [[x, x**2] for x in range(6)]
print(lis)