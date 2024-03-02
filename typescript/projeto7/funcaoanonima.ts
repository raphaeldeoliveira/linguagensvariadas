const nomes = ["Alice", "Bob", "Eve"];

nomes.forEach(function (s) {
    console.log(s.toUpperCase());
})
console.log("------")
nomes.forEach((s) => {
    console.log(s.toUpperCase());
})