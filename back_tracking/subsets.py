def subsets(nums):
    currset, allsets = [], []
    helper(0, nums, currset, allsets)
    return allsets


def helper(i, nums, currset, allsets):
    if i >= len(nums):
        allsets.append(currset.copy())
        return
    currset.append(nums[i])
    helper(i + 1, nums, currset, allsets)

    currset.pop()
    helper(i + 1, nums, currset, allsets)


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
