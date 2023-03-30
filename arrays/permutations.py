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


print(permutations([1, 2, 3, 5, 6, 7, 8, 9, 10]))
