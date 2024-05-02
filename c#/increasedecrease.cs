int x = 5;
int y = 5;
int resultado1, resultado2;

// Pós-incremento
resultado1 = y++;

// Pré-incremento
resultado2 = ++x;

// Comparação direta entre Pré e Pós
int m = 5, n = 5;
int resultado3 = ++m + n++;
Console.WriteLine(resultado3); // 11