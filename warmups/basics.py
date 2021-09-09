# diff21 - given an int n, return the difference between n and 21, return double if diff > 21
def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2