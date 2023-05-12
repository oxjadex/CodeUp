#include<stdio.h>
int main()
{
   int n, i, j;
   int arr[1000]={};
   scanf("%d", &n);
   for (i=1; i<=n; i++)
   {
      scanf("%d", &arr[i]);
   }
   for (i=1; i<=n; i++)
   {
      printf("%d: ", i);
      for (j=1; j<=n; j++)
      {
         if (arr[i]>arr[j] && j!=i)
            printf("> ");
         else if (arr[i]<arr[j] && j!=i)       
            printf("< ");
         else if (arr[i]==arr[j] && j!=i)
            printf("= ");   
      }
      printf("\n");
   }
   return 0;
}
