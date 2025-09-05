# for문 안에서 break 와 continue 쓰기
# 1부터 20까지 합 중 100 넘으면 반복문 중단 : break
# sum = 0
# for i in range(1,21):
#     if sum > 100:
#         break
#     sum = sum + i
# print(sum)

# continue 사용하기
# 홀수는 건너뛰고 짝수만 출력
for i in range(1,11):
    if i%2 == 1:
        continue
    print(i)

    