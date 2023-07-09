def Collatz_seq(n):
    l = [n]
    while(n!=1):
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1

        l.append(n)

    return l

n = int(input())
print(Collatz_seq(n))