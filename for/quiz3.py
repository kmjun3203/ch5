
scores = {'철수':80,'영희':95,'민수':70,'지연':100}

sum =0
for n in scores:
    sum = sum + scores[n]    
avg = sum / len(scores)
print(avg)

sum1 = 0
for value in scores.values():
    sum1 = sum1 + value
print(sum1)
avg1 = sum1 / len(scores)
print(avg1)

cnt = 0
for g in scores:
    if scores[g] >= 90:
        cnt = cnt + 1
print(cnt)