#자리수 구하기 ver1
a=int(input())
count=1
while True:
    answer=a//(10**count)
    if answer>0:
        count+=1
    else:
        break

print(count)

