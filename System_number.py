
def kakaya_sistema():
    total = input()
    a, b, c, d = input(), input(), input(), input()

    n = 9
    while True:
        total_n, a_n, b_n, c_n, d_n = int(total, n), int(a, n), int(b, n), int(c, n), int(d, n)
        if total_n == a_n + b_n + c_n + d_n:
            print(n)
            break
        n += 1

number = int(input())

print(bin(number)[2:].upper())
print(oct(number)[2:].upper())
print(hex(number)[2:].upper())