// Strings
var stringA = ""
print("stringA.isEmpty: ", stringA.isEmpty) // S: true

var stringB = "Gran Cursos!"
print("stringB count: ", stringB.count) // S: 12

print("stringA == stringB: ", stringA == stringB) // S: false

let stringC = "Gran Cursos!"
print("stringB == stringC: ", stringB == stringC) // S: true

for chars in stringC {
    print(chars, terminator: "-")  // S: G-r-a-n- -C-u-r-s-o-s-!-
}

// Arrays
// sintaxe convencional
var valoresA: Array<Int> = []

// sintaxe abreviada
var valoresB: [Int] = []
print("valoresB \(valoresB.count) itens") // S: valoresB 0 itens

// tipo inferido
var valoresC = [1, 2, 3]

valoresC.append(4)

valoresC = []
print("O tipo se mantém: ", type(of: valoresC)) // S: o tipo se mantém: Array<Int>

var tresValores = Array(repeating: 1.2, count: 3)
print("tresValores: ", tresValores) // S: tresValores: [1.2, 1.2, 1.2]
print("type(of: tresvalores): ", type(of: tresValores)) // S: type(of: tresValores): Array<Double>

// juntando arrays com +
var tresValores = Array(repeating: 0.1, count: 3)
var outrosValores = Array(repeating: 2.5, count: 3)
var seisValores = tresValores + outrosValores
print("seisValores: ", seisValores) // S: [0.1, 0.1, 0.1, 2.5, 2.5, 2.5]

// literias de arrays
var listaCompras: [String] = ["Ovo", "Leite"]
print("listaCompras: ", listaCompras) // S: ["Ovo", "Leite"]

// usando inferencia
var listaCompras2 = ["Ovo", "Leite"]
print("listaCompras2: ", listaCompras2) // S: ["Ovo", "Leite"]

// count
print("A lista contém \(listaCompras2.count) items") // S: a lista contém 2 items

// isEmpty
if listaCompras2.isEmpty {
    print("A lista de compras esta vazia")
} else {
    print("A lista de compras não esta vazia")
}

var listaCompras: [String] = ["Ovo", "Leite"]

// apend
listaCompras.append("Farinha")
listaCompras += ["Carne"]
listaCompras += ["Pão", "Frutas"]
print("listaCompras: ", listaCompras)

// alterando valor
listaCompras[2] = "verduras"
print("listaCompras: ", listaCompras)

// enumerated
for (index, valor) in listaCompras.enumerated() {
    print("Item \(index + 1): \(valor)")
}

// substituição por intervalo
listaCompras[2...3] = ["verduras", "frutas"]

// insert - insere na posição especifica
listaCompras.insert("Chocolate", at:  2)
print("listaCompras: ", listaCompras)

// remove - remove o elemento da lista e "tapa o buraco"
listaCompras.remove(at: 3)
print("listaCompras: ", listaCompras)

// removeLast - remove o ultimo elemento da lista
listaCompras.removeLast()
print("removeLast: ", listaCompras.removeLast()) // ele retorna o elemento removido (aparece no print)