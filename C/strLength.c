#include<stdio.h>

size_t strLength(const char*__restrict str);

int main()
{
	char* a = "what";
	printf("%zd ", strLength(a));
}

size_t strLength(const char*__restrict str)
{
	size_t count = 0;
	while (*str++)
		++count;
	return count;
}