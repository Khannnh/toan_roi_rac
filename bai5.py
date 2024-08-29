MOD = 10**9 + 7

def mod_inv(x, mod):
    return pow(x, mod - 2, mod)

def precompute_factorials_and_inverses(max_n, mod):
    factorials = [1] * (max_n + 1)
    inverses = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        factorials[i] = factorials[i - 1] * i % mod
    inverses[max_n] = mod_inv(factorials[max_n], mod)
    for i in range(max_n - 1, 0, -1):
        inverses[i] = inverses[i + 1] * (i + 1) % mod
    return factorials, inverses

def comb(n, k, factorials, inverses, mod):
    if k < 0 or k > n:
        return 0
    return factorials[n] * inverses[k] % mod * inverses[n - k] % mod

def count_solutions(n, m, Y):
    sum_Y = sum(Y)
    S = m - sum_Y
    if S < 0:
        return 0

    max_n = S + n - 1
    factorials, inverses = precompute_factorials_and_inverses(max_n, MOD)

    return comb(S + n - 1, n - 1, factorials, inverses, MOD)

# Ví dụ sử dụng
n = 7
m = 10
Y = [2, 2, 1]
print(count_solutions(n, m, Y))
