# ATRIBUIÇÃO DE VALORES E IMPRESSÃO DE VARIAVEIS
var.1 = c(0,1,2,3)

var.2 <- c("aprenda", "R")

c(TRUE,1) -> var.3

print(var.1)
cat ("var.1 é  ", var.1, "\n")
cat ("var.2 é  ", var.2, "\n")
cat ("var.3 é  ", var.3, "\n")

# S: [1] 0 1 2 3
#    var.1 é  0 1 2 3
#    var.2 é  aprenda R
#    var.3 é  1 1

# Tipo de dados de uma variavel
var_x <- "Olá"
cat("1 - A classe de var_x é ", class(var_x), "\n")
var_x <- 34.5
cat("1 - A classe de var_x é ", class(var_x), "\n")
var_x <- 27L
cat("1 - A classe de var_x é ", class(var_x), "\n")
# S: 1 - A classe de var_x é  character
#    2 - A classe de var_x é  numeric
#    3 - A classe de var_x é  integer

# Listando as variaveis
print(ls())
# S: [1] "arvg" "x" "y" "z"
print(ls(pattern="x"))
# S: [1] "x"

# listando variaveis ocultas
.x <- 1
.x1 <- 1
x <- 1
y <- 2
z <- 'foo'
print(ls())
# S: [1] "arvg" "x" "y" "z"
print(ls(all.name = TRUE))
# S: [1] ".x" ".x1" "arvg" "x" "y" "z"

# Excluindo variaveis
var.3 <- 5
rm(var.3)
print(var.3)
# S: Error in print(var.3) : object 'var.3' not found
#    exit status 1

# Excluindo todas as variaveis juntas
rm(list = ls())
print(ls())
# S: character(0)