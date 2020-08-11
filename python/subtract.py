import sys

var = 0
for i, v in enumerate(sys.stdin.readline().split()):
    if i == 0:
        var = int(v)
    else:
        var -= (int(v))
print(var)
