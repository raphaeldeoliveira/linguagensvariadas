// Atribuindo uma função a uma variavel
val aplicarDesconto: Double => Double = preco => preco * 0.9 // função lambda

// Utiliza a função para aplicar desconto a uma lista de preços
val precos = List(100.0, 200.0, 300.0)
val precosComDesconto = precos.map(aplicarDesconto)

// Mostra os preços com desconto
println(precosComDesconto)
// List(90.0, 180.0, 270.0)