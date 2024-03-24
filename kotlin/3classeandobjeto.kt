class MinhaClasse {
    private var nome: String = "Gran Cursos"

    fun meImprima() {   // esse metodo é publico
        print("Esudando Kotlin no " + nome)
    }
}

fun main(args: Array<String>) {
    val obj = MinhaClasse() // instancia o objeto
    obj.meImprima()
    segundoMain()
    terceiroMain()
    quartoMain()
    quintoMain()
    sextoMain()
}

// classes aninhadas
fun segundoMain() {
    val demo = Externa.Interna().foo()
    print(demo)
}
class Externa {
    class Interna {
        fun foo() = "Olá Gran Cursos!"
    }
}

// classe interna
fun terceiroMain() {
    val demo = SecExterna().Interna().foo()
    print(demo)
}

fun SexExterna {
    private val boasVindas: String = "Bem vindo ao Gran Cursos"
    inner class Interna {
        fun foo() = boasVindas
    }
}

// classe anonima interna
fun quartoMain() {
    var programador: Humano = object: Humano { // Cria uma instancia da interface
        override fun pensar() { // Implementa o metodo pensar
            print("Sou um exemplo de classe anonima interna")
        }
    }
    programador.pensar()
}
interface Humano {
    fun pensar()
}
// Com isso elmina os passos de criar uma classe, extender a interface, instanciar, etc (que precisaria faze no java)

// construtores
// construtor primario (nao contém logica)
fun quintoMain() {
    val pessoa1 = Pessoa("Tiago", 30)
    println("Primeiro nome = ${pessoa1.primeiroNome}")
    println("Idade = ${pessoa1.idade}")
}
class Pessoa(val primeiroNome: String, var idade: Int) {
}

// construtor secundario (contém logica)
fun sextoMain() {
    val humano = Humano("Tiago", 30)
    print("${humano.mensagem} ${humano.primeiroNome}, sua idade é ${humano.idade}")
}
class Humano(val primeiroNome: String, var idade: Int) { // construtor primario
    val mensagem: String = "Olá "
    constructor(nome: String, idade: Int, mensagem: String):this(nome, idade) { // construtor secundario | a parte do ':this(nome, idade)' passa esses parametros para o contrutor primario
    } // a variavel que não é passada para o construtor primario só pode ser acessada dentro do construtor secundario
}

// usando rotulos para sair de loops aninhados
loopExterno@ for (i in 1..3) {
    println("Iteração externa: $i")
    for (j in 1..3) {
        println("   Iteração interna: $j")
        if (i == 2 && j == 2) {
            println("       Terminando o loop externo...")
            break@loopExterno
        }
    }
} 