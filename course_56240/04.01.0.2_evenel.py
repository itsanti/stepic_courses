def even(arr):
    return filter(lambda el: not int(el) % 2, arr)

input()
print(*even(input().split()))
