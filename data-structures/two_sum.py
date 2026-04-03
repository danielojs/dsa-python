# Arrays Practice Problem

nums = [2, 7, 11, 15]

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] + arr[j] == target:
                    return [i, j]

print(two_sum(nums, 10))


def two_sum2(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

print(two_sum2(nums, 9))

