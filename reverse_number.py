def reverse(x: int) -> int:
    if x > 0:
        x = str(x)
        return int(x[::-1])
    else:
        x = str(x)
        return int(x[0] + x[::-1][:-1])