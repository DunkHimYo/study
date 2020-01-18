#include<stdio.h>
#include<stdlib.h>

void FuncRegist(int a,...);


int main()
{
	FuncRegist(2, 1, 2);
}

void FuncRegist(int a,...)
{
	va_list ap;
	__crt_va_start(ap, x);
	printf("%p", ap);
	__crt_va_arg(ap, int);
	printf("%p", ap);
}