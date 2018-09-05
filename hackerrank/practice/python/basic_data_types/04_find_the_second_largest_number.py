def second_largest(lst):
    s = sorted(set(lst))
    return s[-2]    
    
if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    print(second_largest(arr))
