from bisect import bisect_right
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
nn = int(input())
for i in range(nn):
    val = int(input())
    j = bisect_right(nums, val)
    print(j)


