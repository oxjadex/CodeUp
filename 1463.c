#include <stdio.h>
int main ()
{
	int n; 
	int arr[100][100];
	int i, j;
	scanf("%d", &n);
	for (i=n; i>0; i--)
	{
		for (j=0;j<n;j++)
		{
			arr[i][j]=i+j*n;
			printf("%d ", arr[i][j]);
		}printf("\n");
	}
	return 0;
}


