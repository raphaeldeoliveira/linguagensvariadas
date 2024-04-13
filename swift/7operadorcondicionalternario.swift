let altura = 40
let temCabecalho = true
let alturaLinha = altura + (temCabecalho ? 50 : 20)

print(alturaLinha)

// variação do anterior

let altura1 = 40
let temCabecalho1 = true
let alturaLinha1: Int
if temCabecalho {
    alturaLinha1 = altura1 + 50
} else {
    alturaLinha1 = altura1 + 20
}
print(alturaLinha1)