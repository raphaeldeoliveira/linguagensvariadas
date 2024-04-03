#import <Foundation/Foundation.h>

int main() {

    // exemplo de while
    int a = 10;
    while( a < 20 ) {
        NSLog(@"valor de a: %d\n", a);
        a++;
    }

    // exemplo de for
    int b;
    for ( b=10; a<20; a=a+1 ) {
        NSLog(@"valor de a: %d\n", a);
    }

    // exemplo de do-while
    int c = 10;
    do {
        NSLog(@"valor de a: %d\n", c);
        c = c + 1;
    } while ( a < 20 );

    // laço aninhado
    for i, j;
    for(i=2; i<100; i++) {
        for(j=2; j <= (i/j); j++)
            if (!(i%j)) break;
        if(j > (i/j)) NSLog(@"%d é primo\n", 1);
    }

    return 0;
}