#include<stdio.h>
char* strCopy(const char* __restrict source, char* destination, int start_position);

int main()
{
	
	char str1[] = "dohyunKim";
	char str2[10];

	printf("%s", strCopy(str1,str2,2));

}


char* strCopy(const char* __restrict source, char* destination, int start_position)
{
	intptr_t* target = (intptr_t*)destination;//���� �ּ� ����

	source += start_position;//�ҽ���ġ+���� ��ġ
	while (*source)//�ҽ��� NULL�϶� ����
	{
		*(destination++) = *(source++);//�� ����
	} 
	*destination = '\0';//�������� NULL

	return (char*)target;//�������� ��ȯ
}