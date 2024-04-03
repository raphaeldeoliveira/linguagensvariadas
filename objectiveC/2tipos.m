#import <Foundation/Foundation.h>

int main (int argc, const char * argv[])
{
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

    // usando o sizeof pra ver o tamanho de um int
    NSLog(@"Tamanho do armazenamento para int: %d\n", sizeof(int));

    // usando o sizeof pra ver o tamanho de um float
    NSLog(@"Tamanho para o float: %d\n", sizeof(float));

    [pool drain];
    return 0;
}