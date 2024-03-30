// compilador online para teste: https://play.kotlinlang.org/

fun main() {
    // tipos numericos 
    val a: Int = 10000
    val d: Double = 100.00 
    val f: Float = 100.00f
    val l: Long = 1000000004
    val s: Short = 10
    val b: Byte = 1
    println("Seu valor int é "+a)
    println("Seu valor double é "+d)
    println("Seu valor float é "+f)
    println("Seu valor long é "+l)
    println("Seu valor short é "+s)
    println("Seu valor byte é "+b)

    // caracter
    val letra: Char
    letra = 'A'
    println("$letra")

    // string
    var rawString: String = "Essa é uma string crua"
    val escapedString: String = "Essa é uma string de scape \n aaa"
    println("Olá: "+escapedString)
    println("Olá: "+rawString)

    // arrays
    val numeros: IntArray = intArrayOf(1, 2, 3, 4, 5)
    println("Olá, sou um exemplo de array: "+numeros[2])

    /// coleções mutaveis
    val numberos: MutableList<Int> = mutableListOf(1, 2, 3)
    println("Lista mutável: "+numberos)
    numberos.add(4)
    println("Após adição: "+numberos)
    // coleções somente leitura
    val apenasLeitura: List<Int> = numberos
    // se tentar aplciar qualquer metodo na collection acima, ela vai dar erro, pois permite somente leitura -> não vai compilar
    // criando uma lista imutavel com o metodo
    val items = listOf(1, 2, 3, 4)
    println("Primeiro elemento: "+items.first())
    println("ultimo elemento: "+items.last())
    println("Numeros pares da lista: "+items.filter { it % 2 == 0})    
    // 
    val readWriteMap = hashMapOf("foo" to 1, "bar" to 2)
    println(readWriteMap["foo"])
    //
    val strings = hashSetOf("a", "b", "c", "c")
    println("Meu conjunto de valores é: "+strings)
    
    // intervalos (range)
    val i: Int = 2
    for (j in 1..4)
    	println(j)
    if (i in 1..10) {
        println("O numero é "+i)
    }
}