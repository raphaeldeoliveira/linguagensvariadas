// cria uma lista de inteiros
List<int> numeros = new List<int>();

// inicializando uma lista com valores
List<int> valores = new List<int> {1, 2, 3, 4, 5};

numeros.Add(10);

numeros.AddRange(new int[] {20, 30});

Console.WriteLine(numeros[0]);

foreach (int num in numeros) {
    Console.Write(num + " "); // S: 10 20 30
}

numeros.Remove(10);
numeros.RemoveAt(1);

foreach (int num in numeros) {
    Console.Write(num + " "); // S: 20
}