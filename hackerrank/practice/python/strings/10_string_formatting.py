def print_formatted(n):
    # determine width of largest binary
    largest_b = "{:b}".format(n)
    width = len(largest_b)

    for i in range(1, n+1):
        print("{num:{width}} {num:{width}o} {num:{width}x} {num:{width}b}".format(num=i, width=width).upper())

if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
