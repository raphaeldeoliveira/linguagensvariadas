<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.util.Date, java.text.SimpleDateFormat" %> 
<%@ include file="cabecalho.html" %>
<%
    Date agora = new Date();
    SimpleDateFormat formatador = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
    String dataFormatada = formatador.format(agora);
%>
<html>
<head>
    <title>Exemplo Avançado com Diretivas JSP</title>
</head>
<body>
    <h1>Bem-vindo à nossa página!</h1>
    <p>Data e Hora Atual: <%= dataFormatada %></p>
    <%@ include file="rodape.html" %>
</body>
</html>