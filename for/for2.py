# # range : 연속된 숫자를 만들어주는 함수
# # 반환값 : 숫자를 담고 있는 range객체
# # 0부터 9까지의 숫자 10개 반환
# nums = range(10) # 개수
# print(nums)
# # 사용방법
# for n in nums:
#     print(n)

# # 1부터 11까지의 숫자 10개 반환
# nums2 = range(1,11) #마지막 숫자는 포함x
# print(nums2)

# for n in nums2:
#     print(n)

# # 10부터 20까지의 숫자 10개 반환
# nums3 = range(10,21) #마지막 숫자는 포함x
# print(nums3)

# for n in nums3:
#     print(n)

# # range객체를 사용해 '안녕하세요' 10번 출력
# # range의 값이 필요하지 않은 경우
# nums4 = range(10)
# for _ in nums4:
#     print('안녕하세요')

# num1 = input('input : ') #100
# num2 = input('input : ') #200
# num3 = input('input : ') #300

# print(num1 + num2 + num3) #100200300 문자열이기 때문에 100, 200, 300이 합쳐짐

# # 형변환
# num4 = input('input : ')
# num5 = input('input : ')
# num6 = input('input : ')
# sum = int(num4) + int(num5) + int(num6)
# print(sum)

# # 입력과 동시에 형 변환
# num7 = int(input('input : ')) #100
# num8 = int(input('input : ')) #200
# num9 = int(input('input : ')) #300

# print(num7 + num8 + num9) #600

# sum = 0
# # 숫자 입력받고 sum구하기
# num1 = input()
# sum = sum + int(num1)

# num2 = input()
# sum = sum + int(num2)

# num3 = input()
# sum = sum + int(num3)

# 반복문으로 숫자 3개 입력받고 합 구하기
sum = 0
for _ in range(3):
    # 반복할 코드
    num = input()   
    sum = sum + int(num)
print(sum)
