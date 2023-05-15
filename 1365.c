#include <stdio.h>
int main ()
{
	int a, i, j;
	scanf("%d", &a);
	for (i=0; i<a; i++)
	{
		printf("*");
	}
	printf("\n");
	
	for (i=2; i<=a; i++)
	{
		if (a%2==1)
		{
			if (i==a)
			{
				for (j=0; j<a; j++)
					printf("*");
			}
			else if (i<=a/2)
			{
				printf("*");
				for (j=0; j<i-2; j++)
					printf(" ");
				printf("*");
				for (j=0; j<a-(i*2); j++)
					printf(" ");
				printf("*");
				for (j=0; j<i-2; j++)
					printf(" ");
				printf("*");
				printf("\n");
			}
			else if (i==a/2+1)
			{
				printf("*");
				for (j=0; j<i-2; j++)
					printf(" ");
				printf("*");
				for (j=0; j<i-2; j++)
					printf(" ");
				printf("*");
				printf("\n");
			}
			else 
			{
				printf("*");
				for (j=0; j<(a-1)-i; j++)
					printf(" ");
				printf("*");
				for (j=0; j<(i*2)-(a+2); j++)
					printf(" ");
				printf("*");
				for (j=0; j<(a-1)-i; j++)
					printf(" ");
				printf("*");
				printf("\n");
			}
		}
		else 
		{
			if (i==a)
			{
				for (j=0; j<a; j++)
					printf("*");
			}
			else if (i<=a/2)
			{
				printf("*");
				for (j=0; j<i-2; j++)
					printf(" ");
				printf("*");
				for (j=0; j<a-(i*2); j++)
					printf(" ");
				printf("*");
				for (j=0; j<i-2; j++)
					printf(" ");
				printf("*");
				printf("\n");
			}
			else if (i==(a/2)+1)
			{
				printf("*");
				for (j=0; j<i-3; j++)
					printf(" ");
				printf("*");
				for (j=0; j<a-(i*2); j++)
					printf(" ");
				printf("*");
				for (j=0; j<i-3; j++)
					printf(" ");
				printf("*");
				printf("\n");
			}
			else 
			{
				printf("*");
				for (j=0; j<(a-1)-i; j++)
					printf(" ");
				printf("*");
				for (j=0; j<(i*2)-(a+2); j++)
					printf(" ");
				printf("*");
				for (j=0; j<(a-1)-i; j++)
					printf(" ");
				printf("*");
				printf("\n");
			}
		}
	}
	//9/ (2 5) (3 3) (4 1)
	// (6 2), (7 1), (8 0)
	//(6 1), (7 3), (8 5)
	/* 7
	*******
	**   **
	* * * *
	*  *  *
	* * * *
	**   **
	*******
	6
	******1
	**  **2
	* ** *3
	* ** *4
	**  **5
	******6
	8
	********
	**    **
	* *  * *
	*  **  *
	*  **  *
	* *  * *
	**    **
	********
	(6 2), (5, 3)
	(5, 1), (6 0)
	(5 1), (6 3)
	*2 -9
	*/
	//7 (2 3) (3 1)
	return 0;
}


