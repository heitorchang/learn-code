def test_keyboard():
    phailed = []

    count = 1
    for i in range(33, 127):
        if 65 <= i <= 90 or 97 <= i <= 122 or 48 <= i <= 57:
            continue
        print(chr(i), f"code {i}", f"(#{count})")
        u = input()
        if u != chr(i):
            print("phail")
            phailed.append(chr(i))
        print()
        count += 1
    print("phailed:", phailed)


def test_special():
    phailed = []

    count = 1
    for i in [34, 39, 40, 41, 43, 45, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 95, 96, 123, 124, 125, 126]:
        print(chr(i), f"code {i}", f"(#{count})")
        u = input()
        if u != chr(i):
            print("phail")
            phailed.append(chr(i))
        print()
        count += 1
    print("phailed:", phailed)
