a = {x for x in "aaabbbccccd" if x not in "ac"}
print(a)

b = {(3, 2): 3}
print(b[(3, 2)])

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {}?  It is {}.'.format(q, a))

for i in reversed(range(0, 20, 2)):
    print(i)

ab = [i for i in reversed(range(0, 20, 2))]
print(ab)