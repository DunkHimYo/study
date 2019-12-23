#include<stdio.h>

char* strCopy(const char* __restrict source, const char* __restrict destination);

int main()
{
	char str[] = "dohyunKim";
	char str2[10];
	strCopy(str, str2);
	printf("%s", str2);

	
}


char* strCopy(const char* __restrict source, const char* __restrict destination)
{
	while (*source)
	{
		*(destination++) = *(source++);
	}
	return destination;
}