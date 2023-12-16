
def minimum_operations(nums):
    count = 0
    while sum(nums) > 0:
        min_value = min(nums)
        nums = [i - min_value for i in nums if i != 0]
        count += 1
    return count

val = minimum_operations([1, 3, 5])
print(val)


