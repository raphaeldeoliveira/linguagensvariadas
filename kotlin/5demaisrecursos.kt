// classe e interface selada
sealed interface Expr
sealed class MathExpr(): Expr

data class Const(val number: Double) : MathExpr()
data class Sum(val e1: Expr, val e2: Expr) : MathExpr()
object NotANumber : Expr

// generico
class Caixa<T>(t: T) {
    var valor = t
}

val caixa1: Caixa<Int> = Caixa<Int>(1)
val caixa2 = Caixa(2)

// expressões de objeto
val olaMundo = object {
    val ola = "Olá"
    val mundo = "Mundo"
    override fun toString() = "$ola $mundo"
}

// herdando objetos anonimos de supertipos
window.addMouseListener(object: MouseAdapter() {
    override fun mouseClicker(e: MouseEvent) { /*... */ }
    override fun mouseEntered(e: MouseEvent) { /*... */ }
})

// declaração de objetos (singletons)
object DataProviderManager {
    fun registerDataProvider(provider: DataProvider) {
        // ...
    }
    val allDataProviders: Collection<DataProvider>
       get() = // ...
}

DataProviderManager.registerDataProvider(...)

object DefaultListner : MouseAdapter() {
    override fun mouseClicked(e: MouseEvent) { ... }
    override fun mouseEntered(e: MouseEvent) { ... }
}

// delegação
interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() { print(x) }
}

class Derived(b: Base) : Base by b

fun main() {
    println(caixa1.valor)
    println(caixa2.valor)

    println(olaMundo)

    val b = BaseImpl(10)
    Derived(b).print()
}