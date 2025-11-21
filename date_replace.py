from datetime import date

d = date(1991, 2, 5)
new_d = d.replace(year=1992, month=1, day=16)

print(d)
print(new_d)
