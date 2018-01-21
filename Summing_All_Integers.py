s = 'B0012345'
def sum_of_integers(s):
    integers = "".join(filter(str.isdigit,s))
    sum = 0
    for digit in integers:
       digit = int(digit)
       sum += digit
    return sum

print(sum_of_integers(s))
