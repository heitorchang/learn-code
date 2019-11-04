def int_to_ltr(i):
    return chr(96 + i)

def print_rangoli(n):
    # top
    for i in range(n-1, 0, -1):
        print_row(i, n)

    # bottom
    for i in range(n):
        print_row(i, n)
            
def print_row(i, size):
    cols = 4*size - 3 # (2 * (2 * n - 1) - 1)
    row = ['-' for i in range(cols)]
    ctr = (size - 1) * 2 
    # print_row(4, 5) prints --e-d-e--
    for j in range(size-i):
        ltr = int_to_ltr(i+j+1)
        row[ctr - 2*j] = ltr
        row[ctr + 2*j] = ltr
    print("".join(row))
    
if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
