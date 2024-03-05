// enums é um tipo de dado composto por um conjunto de constantes nomeadas
enum UserResponse {
    No = 0,
    Yes = 1,
}
function respond(recipient: string, message: UserResponse) : void {
    console.log(recipient)
}
respond("Professor Tiago", UserResponse.Yes)

// podemos chamar funções dentro de funções. Esse recurso acontece porque no JS
// uma função é considerada um valor (pode transitar de um metodo pra outro, retorno)
function saudar(fn: (a: string) => void) {
    fn("Olá mundo!")
}
// fn é uma função que recebe um parametro do tipo string e retorna um void 
function printToConsole(s: string) {
    console.log(s)
}
saudar(printToConsole)