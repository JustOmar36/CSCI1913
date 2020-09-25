//Omar Masri
//Masri013
public class KnownSpy{
    private String name;
    public CaesarCipher cipher;

    public KnownSpy(String name, CaesarCipher cipher){
        this.name = name;
        this.cipher = cipher;
    }
    
    public String getName(){
        return name;
    }

    public void decrypt(Message message){
       if(message.getFrom().equals(name)){
        message.setMessage(cipher.decrypt(message.getMessage()));
       }
     }
     
     public static boolean isFromSpy(KnownSpy[] names_list, Message message_names){
         for(int i = 0; i < names_list.length; i++){
            if(names_list[i].getName().equals(message_names.getFrom())){
                return true;
            }
         }
         return false;
     }
 }
