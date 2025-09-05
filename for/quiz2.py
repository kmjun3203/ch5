
# for i in range(1,10):
#     a = 3*i
#     print(f'3 X {i} = {a}')

nums = [5,9,3,8,2]
max = nums[0] #가장 큰 값을 저장할 변수
for n in nums:
    if max < n:
        max = n
print('max: ', max)
