// lista imutavel
val listaImutavel = List(1, 2, 3)

listaImutavel(0) = 10 // Erro de compilação

// Uso seguro em ambiente concorrente
listaImutavel.foreach(println)
// 1 2 3
// pode ter quantas threads quiser rodando esse foreach -> não tem efeitos colaterais