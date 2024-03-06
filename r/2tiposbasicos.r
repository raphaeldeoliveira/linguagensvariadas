# exemplificando os tipos basicos do R

# 1- lógico
x <- TRUE
print(class(x))    # vai retornar "logical"

# 2- Numérico
x <- 23.5
print(class(x))    # vai retornar "numeric"

# 3- inteiro
x <- 2L
print(class(x))    # vai retornar "integer"

# 4- Complexo
x <- 2 + 5i
print(class(x))    # vai retornar "complex"

# 5- Caractere
x <- "TRUE"
print(class(x))    # vai retornar "character"

# 6- Raw
x <- charToRaw("Olá")
print(class(x))    # vai retornar "raw"