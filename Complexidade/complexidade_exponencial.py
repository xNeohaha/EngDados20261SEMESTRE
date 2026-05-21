def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# O(2ⁿ) — EVITAR!
def fibonacci_dp(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fibonacci_dp(n-1, memo) \
            + fibonacci_dp(n-2, memo)
    return memo[n]
# O(n) com memoização