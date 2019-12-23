#include<stdio.h>

<<<<<<< HEAD
char* strCopy(const char* __restrict source, const char* __restrict destination);
=======
size_t length(const char* __restrict string);//문자열 길이측정 함수
>>>>>>> f265e02a2579c86fa03a0ef00ea8b7a02455c0d4

int main()
{
	char str[] = "dohyunKim";
<<<<<<< HEAD
	char str2[10];
	strCopy(str, str2);
	printf("%s", str2);

	
=======
	printf("%zd", length(str));//9출력
>>>>>>> f265e02a2579c86fa03a0ef00ea8b7a02455c0d4
}


char* strCopy(const char* __restrict source, const char* __restrict destination)
{
<<<<<<< HEAD
	while (*source)
	{
		*(destination++) = *(source++);
	}
	return destination;
}
=======
	size_t count = 0;//카운트 변수
	while (*string++) ++count;//카운트 루프
	return count;//카운트 리턴
}
>>>>>>> f265e02a2579c86fa03a0ef00ea8b7a02455c0d4
