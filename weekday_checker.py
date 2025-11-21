from datetime import date

s = input("Sana (2019-11-04 14:53:00): ")
y, m, d = map(int, s.split("-"))

kunlar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]

print(kunlar[date(y, m, d).weekday()])
