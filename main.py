def past(h, m, s):
    if h >= 0 and h <= 23 and m >= 0 and m <= 59 and s >= 0 and s <= 59:
        return (h * 3600 + m * 60 + s) * 1000
    else:
        return "Invalid input"