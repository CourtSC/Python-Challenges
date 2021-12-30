def twoSum(nums, target):
    numDict = {}
    for index, num in enumerate(nums):
        if (target - num) in numDict:
            return [numDict[target - num], index]
        else:
            numDict[num] = index

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
