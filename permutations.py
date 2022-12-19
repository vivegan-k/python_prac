def permutions(data, i, length, result=[]):
    if i == length:
        result.append(''.join(data))
    for j in range(i, length):
        data[i], data[j] = data[j], data[i]
        permutions(data,i+1, length, result)
        data[i], data[j] = data[j], data[i]

    return result

print(permutions(list('abc'), 0, len('abc')))