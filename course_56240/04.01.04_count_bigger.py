def count_bigger(arr):
    count = 0
    for ix, el in enumerate(arr[1:]):
        if el > arr[ix]:
            count += 1
    return count

input()
print(count_bigger(list(map(int, input().split()))))
