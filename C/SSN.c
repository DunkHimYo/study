#include<stdio.h>
#include<math.h>
#include<stdlib.h>
//number version

typedef struct {
	unsigned int SSN_front;//�ֹι�ȣ �� �κ�
	unsigned int SSN_back;//�ֹι�ȣ �� �κ�
	unsigned long long SSN_total;//�ֹι�ȣ ��ü
}SSN;

unsigned long long SSN_Calculation(unsigned int SSN_front, unsigned int SSN_back);
//�ֹι�ȣ ��ü ���

int main()
{
	int people = 0;//����� ����
	printf("������� ���ڸ� �Է��ϼ��� : ");
	scanf_s("%d", &people);//����� �Է�
	SSN* a = malloc(people * sizeof(SSN));//����ü ���� �迭 ����
	for (register ptrdiff_t i = 0; i <people; i++)
	{
		scanf_s("%6d-%7d", &(a+i)->SSN_front, &(a+i)->SSN_back);//�ֹ� ��,�� �Է�
		
		(a+i)->SSN_total = SSN_Calculation((a+i)->SSN_front, (a+i)->SSN_back);//�ֹ� ���� ���
		printf("%013llu\n", (a+i)->SSN_total);//���
	}
	


}

unsigned long long SSN_Calculation(unsigned int SSN_front, unsigned int SSN_back)
{
	unsigned long long SSN;//�ֹι�ȣ ��ü�� ��� ����

	SSN = SSN_front;//�ֹι�ȣ �պκ� �ֱ�

	double digit = log10((double)SSN_back) + 1;//�ֹ� �޹ٸ��� ���
	SSN *= (unsigned long long)pow(10, (int)digit);//�ֹ� �պκ�*10^�ֹε޺κ�
	SSN += SSN_back;//�ֹ� ���ڸ� ���ϱ�
	return SSN;
}