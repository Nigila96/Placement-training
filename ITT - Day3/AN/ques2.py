import sys

def solve_construct_array():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    t = int(next(iterator))
    for _ in range(t):
        n = int(next(iterator))
        arr = []
        curr = 1
        for i in range(n):
            arr.append(curr)
            if i % 2 == 0:
                curr += 1
            else:
                curr += 2
        print(*(arr))

if __name__ == '__main__':
    solve_construct_array()
