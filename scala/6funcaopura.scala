// Exemplo de uma função não pura em Scala
var contador = 0 // variavel de estado externo

// Função não pura que incrementa um contador a cada chamada
def incrementarContador(valor: Int): Int = {
    contador += valor // altera o valor do estado externo
    return contador // retorna o novo valor do contador
}

println(contador) // 0
incrementarContador(1)
println(contador) // 1

// Define uma função pura que calcula o quadrado de um numero -> resultado matematicamente previsivel
def quadrado(n: Int): Int = n * n

// Chama a função pura com o mesmo argumento varias vezes
println(quadrado(4)) // Sempre retorna 16, sem efeitos colaterais
println(quadrado(4)) // 16 novamente