#include<stdio.h>
#include<stdbool.h>

bool palindrome(char* __restrict str);//회문 판별
 
int main()
{
	char* a = "woow";
	printf("%s", palindrome(a)==1?"true":"false");//true
}

bool palindrome(char* __restrict str)//회문 판별할 매개 변수
{
	const char* start = str;//시작 위치
	const char* end= str;//종료 위치

	while (*end) end++;//종료 위치 이동

	size_t size = (size_t)(end - start)/2;//크기

	if (*(--end) == '\0' || *start == '\0')//시작 위치와 긑 위치에 null 판별
		return false;
	while (size)
	{
		if (*(start++) != (char)*(end--))//참 거짓 계산
			return false;
		size--;
	}
	return true;
	
}
