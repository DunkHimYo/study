#include<stdio.h>
typedef int E;
#define TEMP(element,x,y) do{element temp;temp=x;x=y;y=temp;}while(0);
void buble(E* array, size_t len, E (*sortFunction)(E*, E*));
void temp(E* pivot, E* target);

E ACDSort(E* n1, E* n2);
E DSDSort(E* n1, E* n2);

int main()
{
	int a = 5;
	int b = 6;
	TEMP(int, a, b);
	printf("%d", a);
}

E ACDSort(E* n1, E* n2)
{
	if (*n1 > *n2)
		return 1;
	else
		return 0;
}

E DSDSort(E* n1, E* n2)
{
	if (*n1 < *n2)
		return 1;
	else
		return 0;
}

void buble(E* array, size_t len, E(*sortFunction)(E*, E*))
{
	for (register ptrdiff_t i = 0; i < (ptrdiff_t)len ; i++)
	{
		for (register ptrdiff_t j = 0; j < (ptrdiff_t)len; j++)
		{
			if (sortFunction(&array[i], &array[j]))
			{
				temp(&array[i], &array[j]);
			}
		}
	}
}
void temp(E* pivot, E* target)
{
	E tem;
	tem = *pivot;
	*pivot = *target;
	*target = tem;
}