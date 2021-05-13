def suffixWithUnit(number):
    if number >= 1000 * 1000:
        return str(number / (1000 * 1000)) + " Mega"
    if number >= 1000:
        return str(number / 1000) + " Kilo"
    return str(number)

print(suffixWithUnit(123))
print(suffixWithUnit(1234))
print(suffixWithUnit(12345))
print(suffixWithUnit(1234567))
print(suffixWithUnit(12345678))