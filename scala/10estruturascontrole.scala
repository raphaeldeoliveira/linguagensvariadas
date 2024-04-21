// IF como expressão, o valor é armazenado em uma variavel
val numero = 10

var resultado = if(numero % 2 == 0) {
    "par"
} else {
    "impar"
}
println(resultado) // S: par

resultado = if (numero % 2 == 0) "Par" else "Impar"
println(resultado) // S: Par

// WHILE

var contador = 5
while (contador > 0) {
    println(contador) // S: 5 4 3 2 1
    contador -= 1
}

// FOR
for (i <- 1 to 5) {
    println(i) // S 1 2 3 4 5
}

// FOR-COMPREHENSIONS
case class Usuario(nome: String, idade: Int)

val usuarios = List(
    Usuario("Joao", 28),
    Usuario("Caio", 33),
    Usuario("Janete", 44),
    Usuario("Glaucia", 23)
)

val vintePoucos = 
    for usuario <- usuarios if usuario.idade >= 20 && usuario.idade < 30
    yield usuario.nome  // filtra e transforma

vintePoucos.forEach(println) // Joao Glaucia

// SEGUNDA FORMA DO FOR-COMPREHENSIONS
def foo(n: Int, v: Int) = // essa estrutura fica como 2 for um dentro do outro 
    for i <- 0 until n // vai de 0 a n
        j <- 0 until n if i + j == v // revebe 0 se i + j for igual a v
    yield (i, j)

foo(10, 10).foreach {
    (i, j) => println(s"($i, $j) ")
    // S: (1, 9) (2, 8) (3, 7) (4, 6) (5, 5) (6, 4) (7, 3) (8, 2) (9, 1) 
}
// printa todas as combinações que a soma de i e j são 10

// FUNÇÕES
def soma(a: Int, b: Int): Int = {
    a + b
}
def concatena(s1: String, s2: String): String = s1 + s2
// First class citizens
val duplica = (x: Int) => x * 2
val resultado = duplica(5) // resultado é 10

// Funções com função lambda
val incrementa = (x: Int) => x + 1
val lista = Lista(1, 2, 3)
val listaIncrementada = lista.map(incrementa) // aplica incrementa a cada elemento

// Funções de alta ordem
def aplicaFuncao(f: Int => Int, valor: Int): Int = f(valor)
val multiplicaPorDois = (x: Int) => x * 2
println(aplicaFuncao(multiplicaPorDois, 5)) // S: 10

// Listas
val imutavel = List(1, 2, 3)
var mutavel = new ListBuffer(1, 2, 3)
// adicionando elementos a uma lista
val novaLista = imutavel :+ 4
mutavel += 4
// removento elementos da lista
val menorLista = imutavel.filter(_ != 1) // remove o elemento 1
mutavel -= 1
// acesso a elementos
val primeiroElemento = imutavel.head
val ultimoElemento = imutavel.last

// Map, Filter e Reducer
val quadrados = imutavel.map(x -> x + x)
val pares = imutavel.filter(x => x % 2 == 0)
val soma = imutavel.reduce((x, y) => x + y)

// Demais exemplos
val numeros = List(1, 2, 3, 4, 5)
val incrementados = numeros.map(_ + 1) // Incrementa cada elemento
val pares = numeros.filter(_ % 2 == 0) // Seleciona apenas numeros pares
val total = numeros.reduce(_ + _) // Calcula a soma total dos elementos
println(s"Total: $total") // S: 15

// Pattern Matching
def exemploMatch(x: Any): String = x match {
    case 1 => "um"
    case "dois" => "um string dois"
    case y: Int => "outro numero: " + y
    case Pessoa("Alice", 30) => "Alice de 30 anos"
    case pessoa: Pessoa => s"Pessoa ${pessoa.nome}, ${pessoa.idade} anos"
    case _ => "algo mais"
}
println(exemploMatch(1))                    // S: um
println(exemploMatch("dois"))               // S: um string dois
println(exemploMatch(10))                   // S: outro numero: 10
println(exemploMatch(Pessoa("Alice", 30)))  // S: Alice de 30 anos
println(exemploMatch(Pessoa("Bob", 25)))    // S: Pessoa: Bob, 25 anos