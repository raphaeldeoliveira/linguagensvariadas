# tipos de dados
# int, float, booleano, string, list, tuple e dictionarie

minha_idade = 22            # int
minha_altura = 1.81         # float
tenho_filho = False         # boolean
primeiro_nome = "Raphael"   # string (str)
tecnologias_favoritas = ['react', 'java', 'python']         # list
data_nascimento = (30, 3, 2001)                             # tuple
meu_endereco = {'rua': 'Nereu Ramos', 'numero': 31, 'bairro': 'centro'}     #dictionarie (dict)

# prints
print("Meu nome é " + primeiro_nome)
print("tenho " + str(minha_idade) + " anos")
print("tenho " + str(minha_altura) + "m de altura")
if (tenho_filho):
    print("tenho filhos")
else :
    print("não tenho filhos")
print("minhas tecnologias faviritas são" + str(tecnologias_favoritas))
print("minha data de nascimento: " + str(data_nascimento))
print("meu endereço: " + str(meu_endereco))
# o metodo str() converte qualquer tipo de dado pra string