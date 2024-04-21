// Long deve ter L no final
val l:Long = 1000000L
// Float deve ter f no final
val f:Float = 10.5f
// Char usa aspa simples
val c:Char = 'a'
// String usa aspas duplas
val s:String = "aaa"
// Unit equivale ao void
def myFunction: Unit = {}

// IMPRIMINDO DADOS
val nome: String = "Scala"
val idade = 15 // tipo inferido

var saldo: Double = 1000.50
saldo += 500.00

// DADOS PRIMITIVOS
val ativo: Boolean = true
val altura: Double = 1.75
val letra: Char = 'A'
val numero: Int = 42

println("Imprimindo " + "Variaveis")
println(s"Nome: $nome")
println(s"Idade: $idade anos ")
println(f"Saldo: atual: $$$saldo%.2f") // Saldo atual: $1500.50
println(s"Ativo: ${ativo}")
println(s"Altura: $altura metros")
println(s"Letra: $lerta")
println(s"Número: $numero")

// VAL x VAR
val pi: Double = 3.14
var raio: Double = 5.0
val area = pi * raio * raio
println(s"A area é: $area")