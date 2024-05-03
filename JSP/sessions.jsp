<!-- Criação e uso da sessão -->
<%
    // Verifica se ja existe uma sessão, se não, cria uma nova
    HttpSession session = request.getSession(true);
    // Armazena dados na sessão
    session.setAttribute("usuario", "NomeDoUsuario");
%>

<!-- Recuperação da sessão -->

<%
    // Recuperando a sessão existente
    HttpSession session = request.getSession(false);
    if (session != null) {
        String usuario = (String) session.getAttribute("usuario");
        out.println("Bem vindo, " + usuario);
    }
%>

<!-- Encerrando uma sessão -->

<%
    HttpSession session = request.getSession(false);
    if (session != null) {
        session.invalidate(); // Encerra a sessão
    }
%>