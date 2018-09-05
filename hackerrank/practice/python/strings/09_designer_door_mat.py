N, M = 9, 27

for i in range(1, N, 2):
    print("---" * ((N-i)//2) + ".|." * i + "---" * ((N-i)//2))
print("-"*((M-7)//2) + "WELCOME" + "-"*((M-7)//2))
for i in range(N-2, -1, -2):
    print("---" * ((N-i)//2) + ".|." * i + "---" * ((N-i)//2))
