def checksign(arr):
    for ix, el in enumerate(arr[1:]):
        if el * arr[ix] > 0:
            break
    else:
        return 'NO'
    return 'YES'

input()
print(checksign(list(map(int, input().split()))))
