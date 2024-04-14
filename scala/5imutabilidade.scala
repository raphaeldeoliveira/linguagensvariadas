// Define uma lista imutavel de numeros
val numeros = List(1, 2, 3, 4, 5)

// Tenta adicionar um elemento a lista (isso cria uma nova lista, a original permanece imutavel)
val novaLista = numeros :+ 6

println(numeros)   // List(1, 2, 3, 4, 5)
println(novaLista) // List(1, 2, 3, 4, 5, 6)