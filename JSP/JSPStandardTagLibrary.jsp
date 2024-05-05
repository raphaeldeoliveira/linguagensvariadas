<!-- Exibindo valores com <c:out> -->
<%@ taglib url="http://java.sun.com/jsp/jstl/core prefix="c" %>
<c:out value="${nomeUsuario}" />

<!-- Iterando com <:forEach> -->

<ul>
    <c:forEach items="${listaProdutos}" var="produto">
        <li>${produto.nome} - ${produto.preco}</li>
    </c:forEach>
</ul>

<!-- Conficionais - IF -->
<c:if test="${logado}">
    Bem-vindo, usuário!
</c:if>

<!-- Conficionais - IF-ELSE -->
<c:choose>
    <c:when test="${usuario.tipo == 'admin'}">
        Painel de controle
    </c:when>
    <c:otherwise>
        Área do Usuario
    </c:otherwise>
</c:choose>

<!-- Formatando -->
<%@ taglib url="http://java.sun.com/jsp/jstl/fmt prefix="fmt" %>
<fmt:formatNumber value="${salario}" type="currency" /> <!-- currency é $ antes -->
<fmt:formatDate value="${dataNascimento}" pattern="dd/MM/yyyy" />

<!-- Criando uma TagLib Customizada -->
<%@ taglib prefix="custom" uri="http://meusite.com/tags"%>
<custom:minhaTag />