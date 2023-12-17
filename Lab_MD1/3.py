
def next_smaller_number(num):
    digits = list(str(num))
    i = len(digits) - 2
    while i >= 0 and digits[i] <= digits[i + 1]:
        i -= 1
    if i == -1:
        return num
    j = len(digits) - 1
    while digits[j] >= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    result = int(''.join(digits))
    return result

number = int(input("Input number:"))
print(next_smaller_number(number))

