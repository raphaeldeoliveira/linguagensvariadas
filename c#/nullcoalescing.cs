int? x = null;
int y = 10;

// Operador de coalescencia Nula
int resultado = x ?? y;
Console.WriteLine("Coalescencia Nula: " + resultado); // Coalescencia Nula: 10

List<int> numeros = null;

int? first = numeros?.FirstOrDefault();
Console.WriteLine("Verificação de nulo: "+first);