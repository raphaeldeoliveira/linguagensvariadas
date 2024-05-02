using System;
class OperadoresAritmeticos {
    static void Main() {
        // Operadores aritméticos
        int soma = 5 + 2;
        int subtracao = 5 - 2;
        int multiplicacao = 5 * 2;
        int divisao = 5 / 2;
        int resto = 5 % 2;

        // Versões abreviadas com operadores de atribuição
        int x = 10;
        x += 5; // Equivale a x = x + 5;
        x -= 5; // Equivale a x = x - 5;
        x *= 5; // Equivale a x = x * 5;
        x /= 5; // Equivale a x = x / 5;
        x %= 5; // Equivale a x = x % 5;

        // Exibindo os resultados
        Console.WriteLine($"Soma: {soma}");
        Console.WriteLine($"Subtração: {subtracao}");
        Console.WriteLine($"Multiplicação: {multiplicacao}");
        Console.WriteLine($"Divisão: {divisao}");
        Console.WriteLine($"Resto: {resto}");
        Console.WriteLine($"Valor final de x: {x}");
    }
}