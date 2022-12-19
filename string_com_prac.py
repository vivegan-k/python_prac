def compression(stri):
    first_char = stri[0]
    res = ""
    val = 1
    for char in stri[1:]:
        if char == first_char:
            val += 1
        else:
            res += first_char + str(val)
            first_char = char
            val = 1
    res += first_char + str(val)
    return res

print(compression('AABBBCCDDDD'))
