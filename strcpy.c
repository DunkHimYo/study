#include<stdio.h>
char* strCopy(const char* __restrict source, char* destination, int start_position);

int main()
{
	
	char str1[] = "dohyunKim";
	char str2[10];

	printf("%s", strCopy(str1,str2,2));

}


char* strCopy(const char* __restrict source, char* destination, int start_position)
{
	intptr_t* target = (intptr_t*)destination;//시작 주소 저장

	source += start_position;//소스위치+시작 위치
	while (*source)//소스가 NULL일때 까지
	{
		*(destination++) = *(source++);//값 대입
	} 
	*destination = '\0';//마지막에 NULL

	return (char*)target;//시작지점 반환
}