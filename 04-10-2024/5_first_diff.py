def first_diff(str1, str2):
    s1 = len(str1)
    s2 = len(str2)
    min_len = min(s1, s2)
    for i in range(min_len):
        if str1[i] != str2[i]:
            return i
    if s1 != s2:
        return min_len
    return -1

print(first_diff("apple", "apPle"))
print(first_diff("Hard", "Harder"))
print(first_diff("title", "title"))