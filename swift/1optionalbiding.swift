// Desempacotamento condicional de optional
// Antes de fazer a atribuição é verificado se o optional tem valor (linha do if)
var minhaString:String? // esse ? ao final indica que é do tipo optional

minhaString = "Gran Cursos!"

if let suaString = minhaString {
    print("sua String - \(suaString)")
} else {
    print("Sua String não contem valor")
}