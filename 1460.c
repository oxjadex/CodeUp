#include <stdio.h>
int main ()
{
	int n; 
	int arr[100][100];
	int i, j;
	scanf("%d", &n);
	for (i=0; i<n; i++)
	{
		for (j=1;j<=n;j++)
		{
			arr[i][j]=i*n+j;
			printf("%d ", arr[i][j]);
		}printf("\n");
	}
	return 0;
}
