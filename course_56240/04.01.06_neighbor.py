def neighbor(arr):
    if len(arr) < 3:
        return 0
    count = 0
    for ix, el in enumerate(arr[1:-1]):
        if arr[ix] < el > arr[ix + 2]:
            count += 1
    return count

input()
print(neighbor(list(map(int, input().split()))))
