#자리수 구하기 ver2
a=int(input())
div=0
count=1
while True:
   div=a/10
   if div>0:
    count+=1
   else:
    break
   a%=10

print(count)

