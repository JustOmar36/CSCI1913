//Omar Masri
//Masri013
public class Message {
    private String from;
    private String to;
    private String message;

    public Message(String from, String to, String message) {
        this.from = from;
        this.to = to;
        this.message = message;
    }

    public String getFrom() {
        return from;
    }

    public String getTo() {
        return to;
    }

    public String getMessage(){
        return message;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public void setMessage(String message){
        this.message = message;
    }

    public String toString(){
        return "Message from: " + from + " to: " + to + " Message: " + message;
    } 
}
