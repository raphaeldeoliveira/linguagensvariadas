// Programação orientada a objetos
// define a classe -> construtor primario
class Pessoa(val nome: String, val idade> Int) 

// Programação funcional
// define uma função que devolve uma lista - recebe uma lista e percorre ela usando a função map e passando um parametro pra função map
// pega esse argumento e devolva esse argumento * 2 - cada elemento é multiplicado por 2
def dobrar(lista: List[Int]): List[Int] = lista.map(_ * 2)

// Uso
val pessoa = new Pessoa("Alice", 30)
val numeros = List(1, 2, 3, 4)
println(dobrar(numeros)) // List(2, 4, 6, 8)