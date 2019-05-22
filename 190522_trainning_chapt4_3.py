def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) #中のタプルの要素１、文字なのでアルファベット順にソート
print(pairs)