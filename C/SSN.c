#include<stdio.h>
#include<math.h>
#include<stdlib.h>
//number version

typedef struct {
	unsigned int SSN_front;//주민번호 앞 부분
	unsigned int SSN_back;//주민번호 뒷 부분
	unsigned long long SSN_total;//주민번호 전체
}SSN;

unsigned long long SSN_Calculation(unsigned int SSN_front, unsigned int SSN_back);
//주민번호 전체 계산

int main()
{
	int people = 0;//사람수 변수
	printf("사람들의 숫자를 입력하세요 : ");
	scanf_s("%d", &people);//사람수 입력
	SSN* a = malloc(people * sizeof(SSN));//구조체 동적 배열 생성
	for (register ptrdiff_t i = 0; i <people; i++)
	{
		scanf_s("%6d-%7d", &(a+i)->SSN_front, &(a+i)->SSN_back);//주민 앞,뒤 입력
		
		(a+i)->SSN_total = SSN_Calculation((a+i)->SSN_front, (a+i)->SSN_back);//주민 총합 계산
		printf("%013llu\n", (a+i)->SSN_total);//출력
	}
	free(a);//


}

unsigned long long SSN_Calculation(unsigned int SSN_front, unsigned int SSN_back)
{
	unsigned long long SSN;//주민번호 전체를 담는 변수

	SSN = SSN_front;//주민번호 앞부분 넣기

	double digit = log10((double)SSN_back) + 1;//주민 뒷바리수 계산
	SSN *= (unsigned long long)pow(10, (int)digit);//주민 앞부분*10^주민뒷부분
	SSN += SSN_back;//주민 뒷자리 더하기
	return SSN;
}
