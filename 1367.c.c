#include <stdio.h>
int main ()
{
	int i, j;
	int n;
	scanf("%d", &n);
	for (i=0; i<n; i++)
	{
		for (j=0; j<n-1-i; j++)
			printf(" ");
		for (j=0; j<n; j++)
			printf("*");
		printf("\n");
	}
	/*
	(0 3) (1 2) (2 1)
	 
	*/
	return 0;
}

