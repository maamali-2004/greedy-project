def statistic(arr):
    result = 0
    for i in range(len(arr)):
        if i == len(arr) - 1 :
            break
        elif arr[i+1] > arr[i]:
            result += arr[i+1] - arr[i]
            arr[i+1] = arr[i]
    return result

arr = []
days = int(input())
for i in range(days):
    x = int(input())
    arr.append(x)
print(statistic(arr))