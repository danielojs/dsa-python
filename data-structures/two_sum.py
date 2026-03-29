# Arrays Practice Problem

nums = [2, 7, 11, 15]
target = 9

output = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            if nums[i] + nums[j] == target:
                output = [i, j]
                break
print(output)

