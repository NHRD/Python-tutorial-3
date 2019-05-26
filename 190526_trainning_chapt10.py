dic = [
    ['Noro', 'Nakao', 'Miyaoka'],
    ['Kimura', 'Miyashita', 'Shibata'],
    ['Matsumoto', 'Tanaka', 'Ivan'],
]

print(list(zip(dic)))

print(list(zip([1, 2, 3], [2, 3, 4])))

from string import Template

sam = Template("$ss is $dd")
print(sam.substitute(ss = "a", dd = "b"))
