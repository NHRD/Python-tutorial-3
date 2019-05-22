def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt + ":")
        if ok in ('y', 'ye', 'yes'):
            #return True
            print("True!")
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

result = ask_ok("Ok to quit??")
print(result)

def f(a, L=[]):
    L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(voltage=1000000, action=100)             # 2 keyword arguments
#parrot(action=100, voltage=1000000, 100)             # 2 keyword arguments
parrot(action=100, voltage=1000000, type=100)             # 2 keyword arguments
#parrot(voltage=1000000, action=100, 100)             # 2 keyword arguments