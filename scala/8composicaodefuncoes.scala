// Define duas funções simples
def dobrar(x: Int): Int = x * 2
def subtrairUm(x: Int): Int = x - 1

// Composição de funções
val dobrarESubtraitUm = dobrar andThen subtrairUm

// Aplica a função composta
val resultadoComposto = dobrarESubtraitUm(5) // (5 * 2) - 1 = 9

println(resultadoComposto) // 9