def get_lps(pat):

    lps = [0]*len(pat)

    i = 1
    while i < len(pat):
        stop = False
        j = 0
        while not stop:

            if pat[i+j] == pat[j]:
                lps[i+j] = lps[i+j-1]+1

            else:
                lps[i+j] = 0
                stop = True
            j += 1

            if i+j >= len(pat):
                stop = True

        i = i+j

    return lps


def search(str, pat):

    m = len(pat)
    n = len(str)
    result = []

    lps = get_lps(pat)
    i = 0

    while i <= (n - m):
        is_finded = True

        for j in range(len(pat)):
            if str[i+j] != pat[j]:
                is_finded = False
                break
        if is_finded:
            result.append(i)
            i += 1

        else:
            i = i + lps[j] + 1

    return result
