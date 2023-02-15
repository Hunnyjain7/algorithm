def sub_string(st):
    sub_strings = set()
    n = len(st)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_strings.add(st[i:j])
    return sub_strings


if __name__ == '__main__':
    print(sub_string("abc"))
