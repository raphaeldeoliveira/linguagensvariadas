#import <Foundation/Foundation.h>

// Declaração de variaveis
extern int a, b;
extern int c;
extern float f;

int main() {
    // Definindo as variaveis
    int a, b;
    int c;
    float f;

    // Inicializando
    a = 10;
    b = 20;
    c = a + b;
    NSLog(@"c: %d \n", c);

    f = 70.0/3.0;
    NSLog(@"f: %f \n", f);

    return 0;

    // saida = c: 30 
    // saida = f: f: 23.333334 
}