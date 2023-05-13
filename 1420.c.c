#include <stdio.h>
int main ()
{
	int a;
	char s[51][11];
	int b[50];
	int i;
	int r;
	int max=0; 
	
	scanf("%d", &a);
	for (i=0; i<a; i++)
	{
		scanf("%s %d", s[i], &b[i]);
		if (b[i]>max)
		{
			max=b[i];
			r=i;
		}	
	}
	b[r]=0;
	max=0;
	for (i=0; i<a;i++)
	{
		if (b[i]>max)
		{
			max=b[i];
			r=i;
 		}
	}
	b[r]=0;
	max=0;
	for (i=0; i<a;i++)
	{
		if (b[i]>max)
		{
			max=b[i];
			r=i;
 		}
	}
	printf("%s", s[r]);
	return 0;
}


