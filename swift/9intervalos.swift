// operador de intervalo fechado
for index in 1...4 {
    print("\(index) vezes 5 é: \(index * 5)")
}

// operador de intervali semi-aberto
let nomes = ["Anna", "Alex", "Brian", "Beatriz"]
let count = nomes.count
for i in 0..<count {
    print("Pessoa \(i) se chama \(nomes[i])")
}

// intervalo unilateral
for nome in nomes[2...] {
    print(nome)
}

for nome in nomes[...2] {
    print(nome)
}
// ... representa até o final. No primeiro é do 2 ate o final e no segundo do inicio até o 2

// variavel com intervalo unilateral
let intervalo = ...5
print(intervalo.contains(7))
print(intervalo.contains(4))
print(intervalo.contains(-1))
print(intervalo)