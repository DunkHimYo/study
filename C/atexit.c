#include<stdio.h>
#include<stdlib.h>

void FuncRegist(void);


int main()
{
	int sel;
	if (!atexit(FuncRegist))
		puts("함수 정상적 등록\n");
	printf("정상종료 1, 비정상 종료 2 : ");
	scanf_s("%d", &sel);
	if (sel == 1)
		exit(EXIT_SUCCESS);
	else
		abort();
}

void FuncRegist(void)
{
	puts("프로그램이 정상적으로 종료되었습니다.");
}