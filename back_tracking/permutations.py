# Time: O(n^2 * n!)
def permutations(nums):
    def helper(i, nums):  # noqa
        if i == len(nums):
            return [[]]

        res = []
        perms = helper(i + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, nums[i])
                res.append(p_copy)
        return res

    return helper(0, nums)


print(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
