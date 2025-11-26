def calc_bundled_temp(n, temp_str):
 
    temp = float(temp_str.replace("*C", ""))

    i = 0
    while i < n:
        temp = temp * 1.1
        i += 1

    temp = round(temp, 1)

    return str(temp) + "*C"
