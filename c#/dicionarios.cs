// criando um dicionario onde a chave é uma string e o valor um int
Dictionary<string, int> idadePessoas = new Dictionary<string, int>();

idadePessoas.add("Maria", 28); // adicionando
idadePessoas["João"] = 30; // adicionando ou alterando

Console.WriteLine(idadePessoas["Maria"]); // acesso pelo nome

idadePessoas.Remove("João")

// iterando sobre o dicionario
foreach (KeyValuePair<string, int> kvp in idadePessoas) {
    Console.WriteLine("Nome: {0}, idade: {1}", kvp.Key, kvp.Value)
}