n = int(input())
arr = list(map(int, input().split()))

low = max((a + 1) // 2 for a in arr)
high = sum(arr)

while low < high:
    t = (low + high) // 2

    cap = t
    ok = True
    for a in arr:
        left = min(cap, a)
        right = a - left
        if right > t:
            ok = False
            break
        cap = t - right

    if ok:
        high = t
    else:
        low = t + 1

print(low)
