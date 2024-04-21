# VETORES
# Criando um vetor
maca <- c('vermelha', 'verde', 'amarela')
print(maca)
# Obtém a classe do vetor
print(class(maca))
# S: [1] "vermelha" "verde" "amarela"
# S: [1] "character"

# LISTAS
lista <- list(c(2, 5, 3), 21.3, sin)
print(lista)
# S: [[1]]
# S: [1] 2 5 3
# S: [[2]]
# S: [1] 21.5
# S: [[3]]
# S: function (x)  .Primitive("sin")

# MATRIZES
M = matrix( c('a', 'a', 'b', 'c', 'b', 'a'), nrow=2, ncol = 3, byrow = TRUE)
print(M)
# S:      [,1] [,2] [,3]
#    [1,]  "a"  "a"  "b"
#    [2,]  "c"  "b"  "a"

# ARRAYS
a <- array(c('verde', 'amarelo'), dim = c(3,3,2))
print(a)

# , , 1

#      [,1]      [,2]      [,3]
# [1,] "verde"   "amarelo" "verde"
# [2,] "amarelo" "verde"   "amarelo"
# [3,] "verde"   "amarelo" "verde"

# , , 2

#      [,1]      [,2]      [,3]
# [1,] "amarelo" "verde"   "verde"
# [2,] "verde"   "amarelo" "amarelo"
# [3,] "amarelo" "verde"   "verde"

# FACTORS
cores_maca <- c('verde', 'verde', 'amarelo', 'vermelho', 'vermelho', 'vermelho', 'verde')
factor_maca <- factor(cores_maca)
print(factor_maca)
print(nlevels(factor_maca))

# S: [1] verde verde amarelo vermelho vermelho verde
#    Levels: amarelo verde vermelho
#    [1] 3

# DATA FRAME
DF <- data.frame(
    genero = c("Masculino", "Masculino", "Feminino"),
    altura = c(152, 171.5, 165),
    peso = c(81, 93, 78),
    idade = c(42, 38, 26)
)
print(DF)

# S:  genero altura peso idade
#    1 Masculino  152.0   81    42
#    2 Masculino  171.5   93    38
#    3  Feminino  165.0   78    26