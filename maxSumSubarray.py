#  the maximum sum subarray problem is the task of finding a contiguous subarray with the largest sum, within a given one-dimensional array A[1...n] of numbers.

'''def maxSequence(arr):
    maxSum = 0
    for i, x in enumerate(arr):
        if x > maxSum:
            maxSum = x
        for y in arr[i + 1: -1]:
            if x + y > maxSum:
                maxSum = x + y
    return maxSum'''

def maxSequence(arr): # Using Kandane's algorithm.
    if len(arr) <= 0:
        return 0
    else:
        maxSum = arr[0]
    currentSum = arr[0]
    for n in arr[1:]:
        currentSum = max(n, currentSum + n)
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum

print(
    maxSequence([-2, 2, 5, -11, 6]), # Should be 7.
    maxSequence([2, -1, 4]), # Should be 5.
    maxSequence([]),
    maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), # Should be 6.
    maxSequence([-2, 1, -3, -4, 1, 1, -1, -2, 1, -5]) # Should be 2.
)