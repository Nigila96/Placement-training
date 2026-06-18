N = int(input())
A = list(map(int, input().split()))

colors = set()
free_users = 0

for rate in A:
    if rate < 400:
        colors.add("gray")
    elif rate < 800:
        colors.add("brown")
    elif rate < 1200:
        colors.add("green")
    elif rate < 1600:
        colors.add("cyan")
    elif rate < 2000:
        colors.add("blue")
    elif rate < 2400:
        colors.add("yellow")
    elif rate < 2800:
        colors.add("orange")
    elif rate < 3200:
        colors.add("red")
    else:
        free_users += 1

base_colors = len(colors)

min_ans = max(1, base_colors)
max_ans = base_colors + free_users

print(min_ans, max_ans)
