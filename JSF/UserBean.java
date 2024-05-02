@ManagedBean // registra que esse bean vai responder ao HTML
@RequestScoped // define que a cada requisiçao é instanciado um novo objeto dessa classe
public class UserBean {
    private String name;

    public UserBean() {
    }
    
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String submit() {
        FacesContext.getCurrentInstance().addMessage(null, new FaceMessage("Dados submetidos com sucesso!"));
        return null;
    }
}