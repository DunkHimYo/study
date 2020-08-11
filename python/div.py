from sys import stdin

for i,v in enumerate(stdin.readline().split()):
    if i==0:
        div=int(v)
    else:
        div/=int(v)
print(div)
