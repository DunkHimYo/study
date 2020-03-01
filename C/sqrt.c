#include<stdio.h>

double sqrt(double a);
int main()
{
	
	printf("%f", sqrt(2));
}

double sqrt(double a)
{
	double x = 1;
	while (1)
	{
		x = (x+a / x) / 2;
		double z = x * x;
		if (a - 0.0005 < x*x && x*x < a + 0.0005)
		{
			break;
		}
	}
	return x;
}