#include<stdio.h>
typedef void(*type)(void);
typedef char* a[5];


void AddProc(void);
void MinusProc(void);
type RetFuncPtr(int sel);



int main()
{
	a b = { "what","are" };
	printf("%s", b[0]);
	return 0;
	
}

void AddProc(void)
{
	int n1, n2;
	printf("���� ���� �� ���� ���� �Է� : ");
	scanf_s("%d %d", &n1, &n2);
	printf("���� ��� : %d\n", n1 + n2);
}
void MinusProc(void)
{
	int n1, n2;
	printf("���� ���� �� ���� ���� �Է� : ");
	scanf_s("%d %d", &n1, &n2);
	printf("���� ��� : %d\n", n1 - n2);
}
void(*RetFuncPtr(int sel))(void)
{
	if (sel == 1)
		return AddProc;
	else
		return MinusProc;
}
