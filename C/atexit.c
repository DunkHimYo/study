#include<stdio.h>
#include<stdlib.h>

void FuncRegist(void);


int main()
{
	int sel;
	if (!atexit(FuncRegist))
		puts("�Լ� ������ ���\n");
	printf("�������� 1, ������ ���� 2 : ");
	scanf_s("%d", &sel);
	if (sel == 1)
		exit(EXIT_SUCCESS);
	else
		abort();
}

void FuncRegist(void)
{
	puts("���α׷��� ���������� ����Ǿ����ϴ�.");
}