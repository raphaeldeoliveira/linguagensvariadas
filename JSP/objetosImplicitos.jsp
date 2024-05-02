<html>
<body>
    <!-- Uso do objeto implícito 'request' para capturar parametros da requisição -->
    O seu IP é: <%= request.getRemoteAddr() %><br>
    O navegador utilizado é: <%= request.getHeader("User-Agent") %>
</body>
</html>