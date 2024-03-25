
// principio da herança
import java.util.Arrays
open class ABC {
    fun falar() {
        print("Olá mundo")
    }
}
class BCD: ABC() {
}
fun main(args: Array<String>) {
    var a = BCD()
    a.falar
    segundoMain()
    terceiroMain()
    quartoMain()
    quintoMain()
    sextoMain()
    setimoMain()
}
// por padrão as classes no kotlin são final (não podem ser extendidas) para
// poder extender usamos o operador 'open' antes da classe

// sobrescrevendo metodos
open class ABC {
    open fun falar () {
        print("Olá mundo")
    }
}
class BCD: ABC() {
    override fun falar () {
        print("Bom dia mundo")
    }
}
fun segundoMain() {
    var a = BCD()
    a.falar
}

interface PessoaInterface {
    var idade: Int
    fun falar() : String // metodo abstrato (nao contem corpo)

    fun saudar() {
        print("Olá alunos")
    }
}

class PessoaImp: PessoaInterface { // implementa a interface
    override var idade: Int = 25
    override fun falar() = "Bom dia"
}

fun terceiroMain() {
    val obj = PessoaImp()
    println("Minha idade é = ${obj.idade}")
    print("Chamando saudar(): ")
    obj.saudar()

    print("chamando falar(): ")
    println(obj.falar())
}

interface A {
    fun mensagenA() {
        println("Metodo da interface A")
    }
}
interface B {
    fun mensagemB() {
        println("Metodo da interface B")
    }
}

class ExemploMultiplasInterfaces: A, B

fun quartoMain() {
    val obj = ExemploMultiplasInterfaces()
    obj.mensagenA()
    obj.mensagemB()
}

// no java uma função nao precisa estar dentor de um objeto. Nesse caso ela fica
// "em nivel superior"
package foo

fun baz() {
    println("bax")
}

class Bar

fun quintoMain() {
    var b: Bar;
    baz();
}

// modificadores de visibilidade I

package foo

private fun foo() { print("Olá") }

public var bar: Int = 5
    private set // isso define que a variavel tem um setter privado, ou seja, só pode ser alterado nesse arquivo

    internal val baz = 6

// modificadores de visibilidade II

open class Externa {
    private val a = 1
    protected open val b = 2
    internal val c = 3
    val d = 4 // public por padrao

    protected class Aninhada {
        public val e: Int = 5
    }
}

class Subclasse: Externa() {
    // a não é visivel
    // b, c, d são visiveis
    // aninhada e é visivel
    override val b = 5 // b é portected
}

class NaoRelacionado(o: Externa) {

}

// colocar uma nova função em um objeto que ja existe

fun MutableList<Int>.troca(index1: Int, index2: Int) {
    val tmp = this[index1]
    this[index1] = this[index2]
    this[index2] = tmp
}

fun sextoMain() {
    val list = MutableListOf(1, 2, 3)
    println(list)
    list.troca(0, 2)

    print(list)
}

// extensão de um objeto
class A {
    companion object {
        fun saudar() : String {
            return ("Bom dia")
        }
    }
}
fun setimoMain() {
    println("Olá " +A.saudar())
}

// classe de dados

data class Livro(val nome: String, val editora: String, var nota: Int)

fun main() {
    val livro: Livro = Livro("Kotlin", "Gran Cursos", 5)
    println("O nome do livro é: " + livro.nome)
    println("Editora: " + livro.editora)
    println("Nota: " + livro.nota)
    livro.nota = 7
    println("Imprimindo tudo: " + livro.toString())
    println("Hashcode: " + livro.hashCode())
}