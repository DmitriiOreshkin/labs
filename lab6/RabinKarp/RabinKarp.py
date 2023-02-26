def search(str, pat):
    m = len(pat)
    n = len(str)
    result = []
    patern_hash = hash(pat)
    for i in range(n - m + 1):
        if hash(str[i: i + m]) == patern_hash:
            if str[i: i + m] == pat:
                # return i
                result.append(i)
    return result
