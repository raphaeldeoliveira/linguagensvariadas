#import <Foundation/Foundation.h>

@interface SampleClass:NSObject
- (void)sampleMethod;
@end

@implementation SampleClass

- (void)sampleMethod {
    NSLog(@"Olá Mundo! \n")
}

@end

int main() {
    NSAutoreleasePoll * poll = [[NSAutoreleasePoll alloc] init];
    /* aqui vai um comentario */
    SampleClass *sampleClass = [[SampleClass alloc]init];
    [sampleClass sampleMethod];
    
    [poll drain];
    return 0;
}

// Tokens em Objective-C

NSLog(@"Olá Mundo! \n");
/*
NSLog
@
(
    "Olá Mundo! \n"
)
;
*/