#include <stdio.h>
int main ()
{
	int h,r, i,j,z;
	scanf("%d %d", &h,&r);
	for (z=0; z<r; z++)
	{
		for (i=0; i<h; i++)
		{
			for (j=0; j<i; j++)
				printf(".");
			printf("*\n");
		}
		for (i=h-1; i>0; i--)
		{
			for (j=1; j<i; j++)
				printf(".");
			printf("*\n");
		}
	}
		
	return 0;
}
