arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
leaders = []

max_right = arr[-1]
leaders.append(max_right)

for i in range(n-2, -1, -1):
    if arr[i] > max_right:
        leaders.append(arr[i])
        max_right = arr[i]
    print(i)
print(*leaders[::-1])


