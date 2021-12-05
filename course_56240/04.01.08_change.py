def change(arr):
    for i in range(0, len(arr) - len(arr) % 2, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

input()
print(*change(list(map(int, input().split()))))
