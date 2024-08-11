def get_all_subsequence(_string, subsequence, i):
    if i != len(_string):
        get_all_subsequence(_string, subsequence, i + 1)

        # include first character
        subsequence += _string[i]
        get_all_subsequence(_string, subsequence, i + 1)
    sub_sequences.add(subsequence)
    return sub_sequences


if __name__ == '__main__':
    sub_sequences = set()
    print(get_all_subsequence("abc", "", 0))
