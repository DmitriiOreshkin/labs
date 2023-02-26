def alphabetGen(str, size):
    alphabet = [-1]*256

    for i in range(size):
        alphabet[ord(str[i])] = i

    return alphabet


def search(str, pat):
    m = len(pat)
    n = len(str)

    alphabet = alphabetGen(pat, m)

    s = 0
    result = []

    while (s <= n-m):
        j = m-1

        while j >= 0 and pat[j] == str[s+j]:
            j -= 1

        if j < 0:
            result.append(s)
            s += (m - (alphabet[ord(str[s+m])] if ((s+m) < n) else 1))
            if (s == n-1):
                break

        else:
            s += max(1, j-alphabet[ord(str[s+j])])
            if (s == n-1):
                break
    return result
