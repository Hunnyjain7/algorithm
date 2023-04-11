""" Longest Common Subsequence (LCS) """


def dfs(s1, s2, i1, i2):
    if i1 >= len(s1) or i2 >= len(s2):
        return 0

    if s1[i1] == s2[i2]:
        return 1 + dfs(s1, s2, i1 + 1, i2 + 1)
    else:
        return max(dfs(s1, s2, i1 + 1, i2), dfs(s1, s2, i1, i2 + 1))


# Time: O(2^(n + m)), Space: O(n + m)
def lcs(s1, s2):
    return dfs(s1, s2, 0, 0)


def dfs2(s1, s2, i1, i2, cache):
    if i1 >= len(s1) or i2 >= len(s2):
        return 0
    if cache[i1][i2] != -1:
        return cache[i1][i2]

    if s1[i1] == s2[i2]:
        cache[i1][i2] = 1 + dfs(s1, s2, i1 + 1, i2 + 1)
    else:
        cache[i1][i2] = max(dfs(s1, s2, i1 + 1, i2), dfs(s1, s2, i1, i2 + 1))
    return cache[i1][i2]


# Time: O(n * m), Space: O(n + m)
def memoization_lcs(s1, s2):
    cache = [[-1] * len(s2) for _ in range(len(s1))]
    return dfs2(s1, s2, 0, 0, cache)


# Time: O(n * m), Space: O(n + m)
def dp(s1, s2):
    cache = [[0] * (len(s2) + 1) for _ in range((len(s1) + 1))]

    for r in range(len(s1)):
        for c in range(len(s2)):
            if s1[r] == s2[c]:
                cache[1 + r][1 + c] = 1 + cache[r][c]
            else:
                cache[1 + r][1 + c] = max(cache[r][1 + c], cache[1 + r][c])
    return cache[-1][-1]


# Time: O(n * m), Space: O(m)
def optimized_dp(s1, s2):
    prev_row = [0] * (len(s2) + 1)

    for r in range(len(s1)):
        curr_row = [0] * (len(s2) + 1)
        for c in range(len(s2)):
            if s1[r] == s2[c]:
                curr_row[c + 1] = 1 + prev_row[c]
            else:
                curr_row[c + 1] = max(prev_row[c + 1], curr_row[c])
        prev_row = curr_row
    return prev_row[-1]


if __name__ == '__main__':
    print(optimized_dp("ADCB", "ABC"))
