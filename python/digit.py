#자리수 구하기 ver1
a=int(input())
div=0
remain=0
count=1
while True:
   div=a/10
   if div>0:
    count+=1
   else:
    break
   a%=10


print(count)

