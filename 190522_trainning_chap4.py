def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end = " ")
        a, b = b, a + b
    #print()

fib(100)

#a = 1000

a = 100

def test(n):
    a = 10
    n = n
    print(n)

print(a)
test(10)

def test2(n):
    list = [1,0]
    #list.append(n)
    return list


print(test2(1))