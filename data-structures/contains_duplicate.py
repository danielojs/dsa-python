# Contains Duplicate Problem

nums = [1, 2, 3, 1]

def contains_duplicate(arr) -> bool:
    unique_nums = set()
    for num in arr:
        if num in unique_nums:
            return True
        unique_nums.add(num)
    return False

print(contains_duplicate(nums))

