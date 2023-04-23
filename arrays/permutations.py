def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def get_permutations(i):
        if i == len(nums):
            return [[]]

        res = []
        perms = get_permutations(i + 1)
        for p in perms:
            res_perms = []
            for j in range(len(p) + 1):
                pcopy = p.copy()
                pcopy.insert(j, nums[i])
                res_perms.append(pcopy)
            res += res_perms
        return res

    return get_permutations(0)


# Time: O(n^2 * n!)
def permutations(nums):
    perms = [[]]

    for i in nums:
        nexts = []
        for j in perms:
            for k in range(len(j) + 1):
                j_copy = j.copy()
                j_copy.insert(k, i)
                nexts.append(j_copy)
        perms = nexts
    return perms


# Permutation Sequence
def get_permutation(n: int, k: int) -> str:  # noqa
    nums = [i for i in range(1, n + 1)]

    factorial = [1] * n
    for i in range(1, n):
        factorial[i] = factorial[i - 1] * i

    k -= 1
    res = []
    i = n - 1
    while nums:
        index = k // factorial[i]
        res.append(str(nums[index]))
        nums.pop(index)
        k = k % factorial[i]
        i -= 1
    return ''.join(res)


print(permute([1, 2, 3]))
