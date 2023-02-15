def sub_sequence(st, sub_str=""):
    if len(st) == 0:
        if sub_str:
            sub_sequences.add(sub_str)
        return
    sub_sequence(st[:-1], sub_str + st[-1])
    sub_sequence(st[:-1], sub_str)
    return sub_sequences


if __name__ == '__main__':
    sub_sequences = set()
    print(sub_sequence("abc"))
