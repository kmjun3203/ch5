# 반복문으로 1부터 10까지 출력
# 단, 숫자가 짝수일때만 출력

i = 1
while i <= 10:
    if i%2 == 0:
        print(i)
     
    i = i + 1

# continue : skip
while i <= 10:
    if i%2 == 1:
        i += 1
        continue
    print(i)
    i = i + 1