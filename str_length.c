#include<stdio.h>

size_t length(const char* __restrict string);//문자열 길이측정 함수

int main()
{
	char str[] = "dohyunKim";
	printf("%zd", length(str));//9출력
}


size_t length(const char* __restrict string)
{
	size_t count = 0;//카운트 변수
	while (*string++) ++count;//카운트 루프
	return count;//카운트 리턴
}
