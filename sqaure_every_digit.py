def square_digits(num):
    digits = ''
    num = str(num)
    for n in num:
        n = int(n)
        n = n * n
        digits += str(n)
    return int(digits)
