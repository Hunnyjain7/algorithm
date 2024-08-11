# Brute Force: O(n^2)
def brute_force(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum


# Kadane's Algorithm: O(n)
# find the largest sum of the contiguous subarray
# The idea of Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum contiguous
# subarray ending at current index and a variable max_so_far stores the maximum sum of contiguous subarray found so far,
# Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if it is
# greater than max_so_far.
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


print(kadanes([1, 5, 3, 0, 59, 10]))
