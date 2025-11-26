def sum_odd_and_even(nums):
    even_sum = 0
    odd_sum = 0

    for n in nums:
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n

    return [even_sum, odd_sum]

# 2 chi vazifa

def top_note(student):
    name = student["name"]
    top = max(student["notes"])
    return {"name": name, "top_note": top}

# 3 chi vazifa

def format_date(date):
    month, day, year = date.split("/")
    return year + day + month

# 4 chi vazifa

class Number:
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Number(" + str(self.value) + ")"

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        return Number(self.value // other.value)

