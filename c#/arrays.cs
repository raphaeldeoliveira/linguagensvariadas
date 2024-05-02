// declarando um array de inteiros com 5 elementos
int[] numeros = new int[5];

// inicializando um array durante a declaração
int[] valores = {1, 2, 3, 4, 5};

// acessando elementos do array
Console.WriteLine(valores[0] + " " + valores[1]); // 1 2

// preenchendo um array com loop
for (int i = 0; i< numeros.Length; i++) {
    numeros[i] = i * 2;
}

// lendo elementos de um array com foreach
foreach (int num in numeros) {
    Console.Write(num + " "); // S: 0 2 4 6 8
}

// declarado um matriz de inteiros
int[,] matriz = new int[2, 3] { {1, 2, 3}, {4, 5, 6}};