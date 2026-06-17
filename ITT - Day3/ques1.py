def check_shelf(n, a):
    unique_types = len(set(a))
    
    def count_blocks(arr):
        blocks = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                blocks += 1
        return blocks

    if count_blocks(a) == unique_types:
        return "YES"

    seen = set()
    first_wrong = -1
    for i in range(n):
        if a[i] in seen and a[i] != a[i-1]:
            first_wrong = i
            break
        seen.add(a[i])
        
    if first_wrong == -1:
        return "YES"

    target_val = a[first_wrong]
    candidates = [first_wrong, first_wrong - 1]
    
    for i in range(n):
        if a[i] == target_val or (i > 0 and a[i] != a[i-1]):
            candidates.append(i)

    for idx1 in candidates:
        for idx2 in candidates:
            if idx1 < idx2:
                a[idx1], a[idx2] = a[idx2], a[idx1]
                if count_blocks(a) == unique_types:
                    return "YES"
                a[idx1], a[idx2] = a[idx2], a[idx1]

    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(check_shelf(n, a))
