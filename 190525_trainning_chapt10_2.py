import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

p = zlib.decompress(t)
print(len(p))
print(p)

from timeit import Timer
a = Timer("t=a; a=b; b=t", "a=1; b=2").timeit()
print(a)
b = Timer("a, b = b, a", "a=1; b=2").timeit()
print(b)