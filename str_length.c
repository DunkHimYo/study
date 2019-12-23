#include<stdio.h>

size_t length(const char* __restrict string);

int main()
{
	char str[] = "dohyunKim";
	printf("%zd", length(str));
}


size_t length(const char* __restrict string)
{
	size_t count = 0;
	while (*string++) ++count;
	return count;
}