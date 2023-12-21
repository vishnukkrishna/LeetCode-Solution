"""  2441. Largest Positive Integer That Exists With Its Negative  """


def findMaxK(nums):
        nums = sorted(nums, reverse=True)
        for i in nums:
            if -1 * i in nums:
                  return i
        return -1



nums = [-1,10,6,7,-7,1]
print(findMaxK(nums))