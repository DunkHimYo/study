#include<stdio.h>

typedef int E;

#define SWAP(element,x,y) do{element temp;temp=x;x=y;y=temp;}while(0);

void bubble(E* array, ptrdiff_t len, E(*sortFunction)(E*, E*));
void temp(E* pivot, E* target);
void OddOrEven(E* array, ptrdiff_t len, E(*sortFunction)(E*, E*));

E ACDSort(E* n1, E* n2);
E DSDSort(E* n1, E* n2);


int main()
{
	E a[] = { 5,2,3,6,7,4 };
	ptrdiff_t size = sizeof(a) / sizeof(E);

	OddOrEven(a, size, DSDSort);
	

	for (register ptrdiff_t i = 0; i < size; i++)
		printf("%d ", a[i]);
}

E ACDSort(E* n1, E* n2)
{
	if (*n1 < * n2)
		return 1;
	else
		return 0;
}

E DSDSort(E* n1, E* n2)
{
	if (*n1 > *n2)
		return 1;
	else
		return 0;
}

void bubble(E* array, ptrdiff_t len, E(*sortFunction)(E*, E*))
{
	for (register ptrdiff_t i = 0; i < len; i++)
	{
		for (register ptrdiff_t j = 0; j < len; j++)
		{
			if (sortFunction(&array[i], &array[j]))
			{
				SWAP(E, array[i], array[j]);
			}
		}
	}
}

void OddOrEven(E* array, ptrdiff_t len, E(*sortFunction)(E*, E*))
{
	ptrdiff_t even = 0;
	for (register ptrdiff_t i = 0; i < len ; i++)
	{
		ptrdiff_t pivot = i;
		for (register ptrdiff_t j = i; j < len-1; j++)
		{
			if (!(array[j] % 2))
			{
				pivot++;
			}
			else
			{
				even++;
				break;
			}
		}
		SWAP(E, array[pivot], array[i]);

	}

	if (sortFunction != NULL)
	{
		bubble(array, len-even, sortFunction);
		bubble(array + len-even, even, sortFunction);
	}
}