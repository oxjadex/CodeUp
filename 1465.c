#include <stdio.h>
int main ()
{
	int n, m; 
	int arr[100][100];
	int i, j;
	scanf("%d %d", &n, &m);
	for (i=0; i<n; i++)
	{
		for (j=0; j <m;j++)
		{
			arr[i][j]=(n-i-1)*m+j+1;
			printf("%d ", arr[i][j]);
		}printf("\n");
	}
	return 0;
}



