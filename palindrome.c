#include<stdio.h>
#include<stdbool.h>

bool palindrome(char* __restrict str);
 
int main()
{
	char* a = "woow";
	printf("%s", palindrome(a)==1?"true":"false");
}

bool palindrome(char* __restrict str)
{
	const char* start = str;
	const char* end= str;

	while (*end) end++;

	size_t size = (size_t)(end - start)/2;

	if (*(--end) == '\0' || *start == '\0')
		return false;
	while (size)
	{
		if (*(start++) != (char)*(end--))
			return false;
		size--;
	}
	return true;
	
}