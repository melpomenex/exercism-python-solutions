
def distance(x, y):
    """Counts the differences in two sequences of DNA"""
    if len(x) != len(y):
        raise ValueError("The two strings are not of equal length.")
    return sum(1 for a,b in zip(x, y) if a != b)
