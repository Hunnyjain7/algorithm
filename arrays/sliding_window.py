def sliding_window(nums):
    """ Return the left and right index of the max subarray sum,
    assuming there's exactly one result (no ties).
    Sliding window variation of Kadane's: O(n)
    :param nums:
    :return:
    """
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R
    return [maxL, maxR]


def close_duplicates_brute_force(nums, k):
    """ Check if array contains a pair of duplicate values,
    where the two duplicates are no farther than k positions from
    eachother (i.e. arr[i] == arr[j] and abs(i - j) + 1 <= k).
    O(n * k)
    :param nums:
    :param k:
    :return:
    """
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


def close_duplicates(nums, k):
    """ Same problem using sliding window.
    O(n)
    :param nums:
    :param k:
    :return:
    """
    window = set()  # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


# Find the length of longest subarray with the same
# value in each position: O(n)
def longest_subarray(nums):
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R - L + 1)
    return length


# Find length of the minimum size subarray where the sum is
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)
def shortest_subarray(nums, target):
    L, total = 0, 0
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length
