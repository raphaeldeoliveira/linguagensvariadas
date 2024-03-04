/* podemos criar type alias */
/* exemplo 1 */
type Ponto = {
    x: number;
    y: number;
}
function printCoordenate(pt: Ponto) {
    console.log("The coordinate x is " + pt.x);
    console.log("The coordinate y is " + pt.y);
}
/* exemplo 2 */
type ID = number | string
/* type alias tambem podem ser extendidos */
type Enimal = {
    name: string
}
type Urso = Enimal & {
    honey: boolean
}

/* interface faz a mesma coisa: apelida tipos */
interface Point {
    x: number;
    y: number;
}
function printCoor(pt: Point) {
    console.log("The coordinate x is " + pt.x);
    console.log("The coordinate y is " + pt.y);
}
printCoor({x:100, y:100})
/* interfaces podem ser extendidas com extends */
interface Animal {
    name: string
}
interface Bear extends Animal {
    honey: boolean
}

/* adicionando novos campos a uma interface */
interface Window {
    title: string
}
interface Window {
    ts: number
}

/* asserção de tipo -> assumir que um valor é algo é verdadeiro independente do conteudo */
/* asserções são feitos com as ou colocando o tipo antes entre <> */
const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement
const myCanvas2 = <HTMLCanvasElement>document.getElementById("main_canvas")

/* tipos literais servem para definir um valor especifico de variavel como um tipo isso é
util quando queremos restringir um conjunto de valores*/
const stringImutavel = "foo" // o type disso vai ser "foo"
// ex2:
let xo: "olá" = "olá"
xo = "olá";
//xo = "mundo" não é possivel ja que a variavel somente aceita "olá"
// ex3:
function printText(s: string, alignment: "left" | "right" | "center") {
    console.log(s + " is align to " + alignment)
}
printText("Hello", "left") 
//printText("Legal", "cenre") daria erro
// ex4:
function compare(a: string, b:string): -1 | 0 | 1 {
    return a === b ? 0: a > b ? 1 : -1;
}
// acima estamos definindo o tipo de retorno com tipos literais