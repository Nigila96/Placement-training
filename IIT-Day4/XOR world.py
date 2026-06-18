A, B = map(int, input().split())

def f(X):
    if X % 4 == 0:
        return X
    elif X % 4 == 1:
        return 1
    elif X % 4 == 2:
        return X + 1
    else:
        return 0

print(f(B) ^ f(A - 1))
