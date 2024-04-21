# OPERADORES ARITMETICOS

# + - Adiciona dois vetores
v <- c(2,5.5,6)
t <- c(8, 3, 4)
print(v+t)
# S: [1] 10.0  8.5  10.0

# - - Subtrai o segundo vetor do primeiro
print(v-t)
# S: [1] -6.0  2.5  2.0

# * - Multiplica dois vetores
print(v*t)
# S: [1] 16.0  16.5  24.0

# / - Divide o primeiro vetor pelo segundo
print(v/t)
# S: [1] 0.250000 1.833333 1.5000000

# %% - Retorna o resto da divisao do primeiro vetor pelo segundo
print(v%%t)
# S: [1] 2.0 2.5 2.0

# %/% - Retorna o quociente da divisao do primeiro vetor pelo segundo
print(v%/%t)
# S: [1] 0 1 1

# ^ - Retorna o primeiro vetor elevado ao segundo vetor
print(v^t)
# S: [1] 256.000 166.375 1296.000

# OPERADORES RELACIONAIS
v <- c(2,5.5,6,9)
t <- c(8, 2.5, 14, 9)

print(v>t)
# S: [1] FALSE TRUE FALSE FALSE

print(v<t)
# S: [1] TRUE FALSE TRUE FALSE

print(v==t)
# S: [1] FALSE FALSE FALSE TRUE

print(v<=t)
# S: [1] TRUE FALSE TRUE TRUE

print(v>=t)
# S: [1] FALSE TRUE FALSE TRUE

print(v!=t)
# S: [1] TRUE TRUE TRUE FALSE

# OPERADORES LÓGICOS
v <- c(3,1,TRUE,2+3i)
t <- c(4,1,FALSE,2+3i)

print(v&t)
# S: [1] TRUE TRUE FALSE TRUE

print(v|t)
# S: [1] TRUE TRUE FALSE TRUE

print(!v)
# S: [1] FALSE TRUE FALSE FALSE

print(v&&t)
# S: [1] TRUE

print(v||t)
# S: [1] FALSE

# OPERADORES DIVERSOS

# : - cria uma sequencia de numeros 
v <- 2:8
print(v)
# S: [1] 2 3 4 5 6 7 8

# %in% - identifica se um elemento pertence a um vetor
v1 <- 8
12 -> v2
t <- 1:10
print(v1 %in% t)
print(v2 %in% t)
# S: [1] TRUE
#    [1] FALSE

# %*% - multiplica uma matriz por sua transposta
M = matriz( c(2,6,5,1,10,4), nrow = 2, ncol = 3, byrow = TRUE)
t = M %*% t(M)
print(t)
# S: [,1] [,2]
#    [1,]  65   82
#    [2,]  82  117