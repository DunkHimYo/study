#include<stdio.h>

double InchToCm(double inch);
double CmToInch(double cm);

int main()
{
	printf("%lf", CmToInch(1));

}

double InchToCm(double inch)
{
	return inch / 3.24;
}

double CmToInch(double cm)
{
	return cm * 3.24;
}