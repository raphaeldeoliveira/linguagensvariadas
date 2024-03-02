/* declaramos os tipos na variavel com : seguido do tipo */

function saudar(pessoa: string, data: Date) {
    console.log(`Olá ${pessoa}, hoje é  ${data.toDateString()}!`)
}

saudar("Thiago", new Date())