def pos_sum(arr):
    return sum(1 for el in map(int, arr) if el > 0)

input()
print(pos_sum(input().split()))
