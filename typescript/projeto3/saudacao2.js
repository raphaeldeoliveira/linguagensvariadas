/* declaramos os tipos na variavel com : seguido do tipo */
function saudar(pessoa, data) {
    console.log("Ol\u00E1 ".concat(pessoa, ", hoje \u00E9  ").concat(data.toDateString(), "!"));
}
saudar("Thiago", new Date());
