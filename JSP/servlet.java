// Método da Servlet
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    String mensagem = "Olá, JSP!";
    request.setAttribute("msg", mensagem); // Passando uma mensagem para o JSP
    requestDispatcher dispatcher = request.getRequestDispatcher("/WEB-INF/pagina.jsp");
    dispatcher.forward(request, response); // Encaminha para o JSP
}




