import sys

def solve_seating_arrangement():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    t = int(next(iterator))
    for _ in range(t):
        n = int(next(iterator))
        x = int(next(iterator))
        s = int(next(iterator))
        u = next(iterator)
        
        dp = {(0, 0): 0}
        for char in u:
            next_dp = {}
            for (j, k), val in dp.items():
                next_dp[(j, k)] = max(next_dp.get((j, k), -1), val)
                if char == 'I':
                    if j < x:
                        next_dp[(j+1, k)] = max(next_dp.get((j+1, k), -1), val + 1)
                elif char == 'E':
                    if k < j * (s - 1):
                        next_dp[(j, k+1)] = max(next_dp.get((j, k+1), -1), val + 1)
                elif char == 'A':
                    if j < x:
                        next_dp[(j+1, k)] = max(next_dp.get((j+1, k), -1), val + 1)
                    if k < j * (s - 1):
                        next_dp[(j, k+1)] = max(next_dp.get((j, k+1), -1), val + 1)
            dp = next_dp
        print(max(dp.values()))

if __name__ == '__main__':
    solve_seating_arrangement()
