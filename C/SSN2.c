#include<stdio.h>
#include<string.h>
//char version
typedef struct {
	unsigned char* SSN_front;//�ֹι�ȣ �� �κ�
	unsigned char* SSN_back;//�ֹι�ȣ �� �κ�
	unsigned char SSN_total[15];//�ֹι�ȣ ��ü
}SSN;

int main()
{
	SSN a;
	scanf_s("%s", a.SSN_total, 15);
	a.SSN_front = strtok_s(a.SSN_total, "-", &a.SSN_back);
	printf("%s-%s", a.SSN_front,a.SSN_back);
	
}