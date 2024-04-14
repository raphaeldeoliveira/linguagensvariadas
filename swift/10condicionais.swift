// IF
var varA = 10
if varA < 20 {
    print("varA é menor que 20")
}

// IF-ELSE
varA = 100
if varA < 20 {
    print("varA é menor que 20")
} else {
    print("varA não é menor que 20")
}
print("varA vale \(varA)")

// IF-ELSEIF-ELSE
if varA == 20 {
    print("varA vale 20")
} else if varA == 50 {
    print("varA vale 50")
} else {
    print("nenhum dos valores bate")
}
print("varA vale \(varA)")

// SWITCH
var index = 10
switch index {
    case 100:
        print("valor de index é 100")
        fallthrough
    case 10,15:
        print("valor de index esta entre 10 e 15")
        fallthrough
    case 5:
        print("valor de index é 5")
    default:
        print("caso padrão")
}

// FOR-IN
var inteiros:[Int] =[10, 20, 30]
for index in inteiros {
    print("O valor de index é \(index)")
}

// WHILE
var index = 1
while index < 5 {
    print("Valor de index é \(index)")
    index = index + 1
}

// REPEAT
index = 1
repeat {
    print("Valor de index é \(index)")
    index = index + 1
} while index < 5

// instrução CONTINUE
index = 1
repeat {
    index = index + 1
    if (index == 5) {
        continue
    }
    print("O valor de index é \(index)")
} while index < 10
// não vai printar o 5 (vai pular por conta do continue)
// 2, 3, 4, 6, 7, 8, 9

// instrução BREAK
index = 1
repeat {
    index = index + 1
    if (index == 5) {
        break
    }
    print("O valor de index é \(index)")
} while index < 10
// vai printar até o 4 (2, 3, 4)

