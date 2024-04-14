// Define uma função de alta ordem que recebe uma função e um valor e aplica a função ao valor duas vezes
def aplicarDuasVezes(funcao: Int => Int, valor: Int): Int = funcao(funcao(valor))
// função definida de forma recursiva

// Define uma função cimples que duplica o numero recebido
def duplicar(x: Int): Int = x + x

// Utiliza a função de alta ordem, o retorno da 1 invocação será usado como parametro da segunda invocação
val resultado = aplicarDuasVezes(duplicar, 10)

println(resultado) // 40