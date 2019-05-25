import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

p = zlib.decompress(t)
print(len(p))
print(p)

zlib.crc32(s)

