// IF
int x = 9;
if (x % 3 == 0) {
    Console.WriteLine("sim");
} else {
    Console.WriteLine("sim");
}

// FOR
for (int i = 0; i < 5; i++) {
    Console.WriteLine(i);
}

// FOREACH
int[] numeros = {1, 2, 3, 4, 5};
foreach (int numero in numeros) {
    Console.Write(numero + " "); // S: 1 2 3 4 5
}
List<string> frutas = new List<string> {"maçã", "banana", "cereja"};
foreach (string fruta in frutas) {
    Console.Write(fruta + " "); // S: maçã banana cereja
}

// WHILE
int numero = 10;
while (numero > 0) {
    Console.WriteLine(numero); // S: 10, 7, 4, 1
    numero -= 3;
}