#include <stdio.h>

int main()
{

    int a, b;

    scanf("%d,%d", &b, &a);
    int c = a / b;
    int d = b / a;
    if (c > d)
        printf("1");
    else
        printf("2");
    printf("%d", a + b);
    printf("%d",a-b);

    return 0;
}