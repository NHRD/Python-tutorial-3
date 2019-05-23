sample = [1, 2, 3,]
ext = [1, 2, 3]
for n in range(2):
    sample.extend(ext)
    #if len(sample) >= 6:
        #break

print(sample)

sample2 = [1, 1, 1, 2, 3, 2, 1]
print(sample2.index(2, 1, 6))
print(sample2.index(2, 4, 6))

sample3 = [1, 2, 3]
ext1 = (4, 5, 6)
ext2 = {4:7, 5:8, 6:9}
for b in range(2):
    sample3.extend(ext1)
    print(sample3)
    sample3.extend(ext2)
    print(sample3)
    #if len(sample) >= 6:
        #break

