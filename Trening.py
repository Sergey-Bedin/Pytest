n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
b = n+m-t-x
d = n+k-t-z
c = m+k-t-y
two = b+d+c

o_n = n-b-d-t
o_m = m-b-c-t
o_k = k-d-c-t
one = o_n + o_k + o_m

zero = a - (b+d+c+t+o_k+o_m+o_n)
print(one)
print(two)
print(zero)