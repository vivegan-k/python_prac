'''
def product_of_arr(li):
    result = []
    product = 1
    for i in range(len(li)):
        for j in range(len(li)):
            if i != j:
                product *= li[j]
        result.append(product)
        product = 1
    print(result)

'''


'''
li = [1,2,3,4]

prefix = []
postfix = []
output = []

product1 = li[0]
for i in range(len(li)):
    if len(prefix) == 0:
        prefix.append(li[i])
    else:
        product1 *= li[i]
        prefix.append(product1)
print(prefix)

product2 = li[len(li)-1]
for i in range(len(li)-1, -1, -1):
    if len(postfix) == 0:
        postfix.append(li[i])
    else:
        product2 *= li[i]
        postfix.insert(0,product2)
print(postfix)

for i in range(len(li)):
    if i == 0:
        output.append(postfix[i+1])
    elif i == len(li)-1:
        output.append(prefix[i-1])
    else:
        output.append(prefix[i-1]*postfix[i+1])
print(output)
'''
def product_of_arr(nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

print(product_of_arr([1,2,3,4]))

