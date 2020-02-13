palindrom=input('단어를 입력하세요 : ')
check=True
for i in range(len(palindrom)//2):
    if palindrom[i]!=palindrom[len(palindrom)-i-1]:
        print('회문판별X')
        check=False

if check==True:
    print('회문판별O')

    