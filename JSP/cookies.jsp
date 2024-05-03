<!-- Criação e uso da Cookies -->
<%
    Cookie cookie = new Cookie("usuario", "NomeDoUsuario");
    cookie.setMaxAge(60*60*24); // Define a validade do cookie para 1 dia
    response.addCookie(cookie); // Envia o cookie para o cliente
%>

<!-- Recuperando Cookies -->

<%
    Cookie[] cookies = request.getCookies();
    String usuario = null;
    if (cookies != null) {
        for (Cookie cookie : cookies)
            if (cookie.getName().equals("usuario"))
                usuario = cookie.getValue();
    }
    if (usuario != null) {
        out.println("Bem vindo de volta, " + usuario);
    }
%>

<!-- Excluindo um Cookie -->

<%
    Cookie cookie = new Cookie("usuario", "");
    cookie.setMaxAge(0);
    response.addCookie(cookie);
%>