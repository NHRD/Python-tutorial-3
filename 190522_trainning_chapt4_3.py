def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) #中のタプルの要素１、文字なのでアルファベット順にソート
print(pairs)

def test(n):
    return lambda x:x+n

result = test(10)
print(result(10))
print(result(10))
print(result(0))

def f(ham: int, eggs: int = 3) -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    ham1 = str(ham)
    eggs1 = str(eggs)
    return ham1 + ' and ' + eggs1

f(3)
