for $x in doc("exemplo.xml")/livraria/livro
where $x/@tipo = "Literatura"
order by $x/titulo
return $x/titulo
(: exemplo :)