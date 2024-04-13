var a: Int?
let b = 10
let c = (a ?? b) // se a tiver algum valor c = a, senão c = b
print(c) // S: 10

let d = a != nil ? a! : b // é equivalente ao (a ?? b)
// a! faz o desempacotamento de a
print(d) // S: 10