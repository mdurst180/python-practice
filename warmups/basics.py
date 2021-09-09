# diff21 - given an int n, return the difference between n and 21, return double if diff > 21
def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False
def near_hundred(n):
    return True