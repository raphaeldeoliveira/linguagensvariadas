let $biblioteca := doc('biblioteca.xml')/biblioteca
for $livro in $biblioteca/livro
where $livro/categoria = "Literatura Nacional"
return 
    <detalhes>
        <titulo>{ $livro/titulo/text() }</titulo>
        <autor>{ $livro/autor/text() }</autor>
    </detalhes>