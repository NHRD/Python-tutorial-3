import statistics

data = [0, 1, 2, 3, 4, 5, 6]

print(statistics.mean(data))
print(statistics.variance(data))

from urllib.request import urlopen
with urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl") as response:
    for line in response:
        line = line.decode("utf-8")
        if "EST" in line or "EDT" in line:
            print(line)

from datetime import date

now = date.today()
birthday = date(1910, 5, 10)
age = now - birthday
print(age.days)
print(int(age.days)//365)
print(age.days//365)