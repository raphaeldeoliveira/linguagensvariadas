/* definindo o tipo de um objeto (na assinatura do paramtro) */
function printCoord(pt: {x: number; y:number}) {
    console.log("O valor de x é " + pt.x);
    console.log("O valor de y é " + pt.y);
    console.log(typeof(pt))
}
printCoord({x: 3, y: 7})

/* pra definir um parametro como opcional usamos ? junto a variavel */
function imprimeNome(obj: {first: string, last?: string}) {
    console.log("firstName: " + obj.first)
    obj.last ? console.log("lastName: " + obj.last) : null
}
imprimeNome({first: "bob"})
imprimeNome({first: "bob", last: "esponja"})

/* podemos criar parametros com tipos de união */
/* no exemplo a baixo o parametro id pode receber um tipo string ou number com operador ou (|) */
function printId(id: number | string) {
    console.log("Your ids is: " + id); 
}
printId(101)
printId("202")
/* no caso de termos uma função onde temos metodos que nao podem ser usados pelos dois tipos
teremos de fazer estreitamento (criar logica para nao poder ser aplicado metodo em tipo errado) */
/* codigo com erro (sem estreitamento) */
function printId2(id: number | string) {
    console.log(id.toUpperCase())
}
/* codigo correto (com estreitamento) */
function printId3(id: number | string) {
    if (typeof id === 'string') {
       console.log(id.toUpperCase());
    } else {
       console.log(id)
    }
}

let x = "aaa"