#include<stdio.h>
#include<string.h>
//char version
typedef struct {
	unsigned char* SSN_front;//주민번호 앞 부분
	unsigned char* SSN_back;//주민번호 뒷 부분
	unsigned char SSN_total[15];//주민번호 전체
}SSN;

int main()
{
	SSN a;
	scanf_s("%s", a.SSN_total, 15);
	a.SSN_front = strtok_s(a.SSN_total, "-", &a.SSN_back);
	printf("%s-%s", a.SSN_front,a.SSN_back);
	
}