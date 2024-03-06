# o programa abaixo vai gerar 1000 numeros em distribuição aleatoria, 
# organizalos com base na frequencia e criar um grafico de barras
n <- floor(rnorm(10000, 500, 100))
t <- table(n)
barplot(t)

# destrinchando:
# floor() -> arredonda pra baixo
print(floor(3.8))   # retorna 3

# rnotm() -> gera numeros aleatorios a partir de uma distribuição normal
# (numero de observações, media da distribuição, desvio padrao)
print(rnorm(100, 0, 5))

# table() -> cria uma tabela de frequencia 
amostra <- (1, 2, 3, 3, 3, 2, 1, 4, 5, 2, 3, 5, 4, 1, 2, 3, 2, 3, 2, 3, 4)
print(table(amostra))

