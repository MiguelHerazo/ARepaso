from random import randint
N = 7
M = 11

m = [[randint(1,10) for j in range(M)] for i in range(N)]

for f in m:
    print(f)