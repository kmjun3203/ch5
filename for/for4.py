nums = [1,2,3,4]
# 새로운 리스트
new_nums = []
# nums의 각 요소에 *3을 해서 [3,6,9,12] 만들기
for n in nums:
    # 새로운 리스트에 값 담기
    new_nums.append(n*3)

# 위 코드를 '리스트 컴프리헨션' 이라는 문법으로
# 간단하기 작성
# 새로운 리스트 = [변수 + 반복문]
new_nums = [n*3 for n in nums]

nums1 = [1,2,3,4,5,6,7,8,9,10]
# nums1를 사용해 새로운 리스트 만들기
new_nums1 = []
# nums1에서 짝수만 골라서 new_nums에 담기
for n in nums1:
    if n%2 == 0:
        new_nums1.append(n)
print(new_nums1)
# 위 코드를 '리스트 컴프리헨션' 이라는 문법으로
# 새로운 리스트 = [변수 + for + if]
# 마지막으로 앞에 있는 n을 리스트에 추가
new_nums1 = [n for n in nums1 if n%2 == 0 ]
print(new_nums1)

strings = ['a','bb','ccc','dddd','e']
new_str = []
# 문자열 리스트에서 문자의 크기가 2보다 큰 것을 찾고
# 대문자로 변환해서 new_str에 담기
for n in strings:
    if len(n) > 2:
        new_str.append(n.upper())
print(new_str)
# 위 코드를 '리스트 컴프리헨션' 이라는 문법으로
# 새로운 리스트 = [변수 + for + if]
new_str = [n.upper() for n in strings if len(n) > 2]
print(new_str)