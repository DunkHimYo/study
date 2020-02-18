a=[i for i in range(10)]
a=list(map(lambda x: str(x) if x%3==0 else x,a))
print(a)
