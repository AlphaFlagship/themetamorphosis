#include <stdio.h>
//code chef problem solution
int gcd(number1,number2)//gcd function using euclidean algorithm
{
    long int t;
    if (number1<number2)
    {
        t = number1;
        number1 = number2;
        number2=t;
    }
    while (!(number2==0))
    {
        t=number1;
        number1=number2;
        number2 = t%number2;

    }
    return number1;
} 
int main()
{
    long int i,j=1,x,y;
    long int k,numTestCases;
    scanf("%li",&numTestCases);//taking input for num of cases
    
    
    
    for ( y = 0; y < numTestCases; y++)
    {   
        long long int sum=0,alpha;
        scanf("%li",&k);
        int array1[2*k+1];//creating an array for storing data
        int array2[2*k];
        j=1;
        for ( i = 0; i <= 2*k; i++)//creating a sequence with loop
        {
            array1[i]=k + j*j;
            
            j++;
        }
        for ( x = 0; x <= 2*k; x++)//taking gcd of two terms
        {
            long int temp1,temp2,temp3;
            temp1 = array1[x];
            temp2 = array1[x+1];
            temp3 = gcd(temp1,temp2);
            sum = sum + temp3;//summimg up all gcds
            alpha = temp3;
        }
        sum = sum -alpha;
        printf("%lli ",sum);//print
    }

    return 0;
}
