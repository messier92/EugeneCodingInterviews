def fn(arr):
    # init a list
    ans = []

    for i in range(len(arr)):
        ans.append(arr[i])

    return "".join(ans)

arr = ["A","B","C"]
print(fn(arr))