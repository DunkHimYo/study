#include<stdio.h>
#include<stdarg.h>

typedef char data;

typedef data(*althmetic)(int, ...);

data cal_add(int count, ...);
data cal_mul(int count, ...);
data cal_sub(int count, ...);
data cal_div(int count, ...);
althmetic cal(int select);

enum alth {ad=1,su,mu,di};
int main()
{
	printf("%d",cal(su)(3, 1, 2, 3));
	
	return 0;

}

althmetic cal(int select)
{
	althmetic p;
	switch (select)
	{
	case 1:
		p = cal_add;
		break;
	case 2:
		p = cal_sub;
		break;
	case 3:
		p = cal_mul;
		break;
	case 4:
		p = cal_div;
		break;
	default:
		p = NULL;
	}
	
	return p;

}


data cal_add(int count, ...)
{
	va_list ap;
	va_start(ap, count);
	data sum_value = 0;
	for (register int i = 0; i < count; i++)
	{
		sum_value += (data)va_arg(ap, data);
	}

	va_end(ap);
	return sum_value;

}

data cal_mul(int count, ...)
{
	va_list ap;
	va_start(ap, count);
	data mul_value = 0;
	for (register int i = 0; i < count; i++)
	{
		mul_value *= (data)va_arg(ap, data);
	}

	va_end(ap);
	return mul_value;

}

data cal_sub(int count, ...)
{
	va_list ap;
	va_start(ap, count);
	data sub_value = 0;
	for (register int i = 0; i < count; i++)
	{
		sub_value += (data)va_arg(ap, data);
	}

	va_end(ap);
	return sub_value;
}

data cal_div(int count, ...)
{
	va_list ap;
	va_start(ap, count);
	data div_value = (data)va_arg(ap, data);;
	for (register int i = 0; i < count-1; i++)
	{
		div_value /= (data)va_arg(ap, data);
	}

	va_end(ap);
	return div_value;
}