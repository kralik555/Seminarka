
def euclid_algorithm(a, b):
    while b != 0:
        x = a % b
        a = b
        b = x
    return a


if __name__ == "__main__":
    pass
