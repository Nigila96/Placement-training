import sys

def solve_tatar():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    t = int(next(iterator))
    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))
        s = next(iterator)
        
        counts = [0] * k
        for i in range(n):
            if s[i] == '1':
                counts[i % k] += 1
                
        possible = True
        for c in counts:
            if c % 2 != 0:
                possible = False
                break
                
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve_tatar()
