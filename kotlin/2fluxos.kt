fun main(args: Array<String>) {
    // If-Else
    val a: Int = 5
    val b: Int = 2
    val max: Int
    if (a > b) {
        max = a
    } else {
        max = b
    }
    println("1. O maximo de a e b é: "+max)
    // Mesma coisa que acima, mas como expressão (esta retornando um valor)
    max = if (a > b) a else bar
    println("2. O maximo de a e b é "+max)

    // when
    val x: Int = 5
    when (x) {
        1 -> print("x == 1")
        2 -> print("x == 2")
        else -> {
            print("x não é 1 ou 2")
        }
    }

    // for
    val items = listOf(1, 2, 3, 4)
    for (i in items)
    println("O valor do i: " + i)

    // while
    var x: Int = 0
    while (x <= 10) {
        println(x)
        x++
    }

    // do-while
    var x:Int = 0
    do {
        x = x + 10
        println(x)
    } while(x <= 50)

    // funções
    fun dobro(x:Int):Int {
        return 2*x;
    }

    var x:Int = 10
    println("O dobro de x é: " + dobro(x))

    meuRotulo@ for (x in 1..10) {
        if (x == 5) {
            println("Dentro do bloco if o valor de x é "+x)
            break@meuRotulo
        } else {
            println("Dentro do bloco else o valor de x é: "+x)
            continue@meuRotulo
        }
    }

}