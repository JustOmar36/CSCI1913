//Omar Masri
//Masri013
public class CaesarCipher{
    private int keyRotations;
    private String message;
    


    public CaesarCipher(int keyRotations){
        this.keyRotations = keyRotations;
    }   

    public boolean isValid(){
        if (keyRotations >= 1 && keyRotations <= 25){
            return true;
        }
        return false;
    }

    public String encrypt(String message){
        int temp_int;
        char letter_holder;
        message = message.toLowerCase();
        char[] letters = message.toCharArray();
        for(int i = 0; i < letters.length; i++){//for
            if(Character.isAlphabetic(letters[i]) == true){//if
                temp_int = ((int)(letters[i] + keyRotations) - 'a') %(26);
                letter_holder = (char)(temp_int + 'a');
                letters[i] = letter_holder;
            }//if
            else{//else
                letters[i] = letters[i];
            }//else
            message = new String(letters);
        }//for
        return message;
    }
    public String decrypt(String message){
        int temp_int;
        char letter_holder;
        message = message.toLowerCase();
        char[] letters = message.toCharArray();
        for(int i = 0; i < letters.length; i++){//for
            if(Character.isAlphabetic(letters[i]) == true){//i
                temp_int = ((int)(letters[i] - 'a') - keyRotations);
                if (temp_int <= -1){
                    temp_int += 26;
                }
                letter_holder = (char)(temp_int + 'a');
                letters[i] = letter_holder;
            }//if
            else{//else
                letters[i] = letters[i];
            }//else
            message = new String(letters);
        }//for
        return message;//return
    }
    public String toString(){
        return "Caeser("+keyRotations+")";
    }
    // public static void main(String[] args){
    //     String test = "abcdefghijklmnopqrstuvwxyz";
    //     CaesarCipher testing = new CaesarCipher(1);
    //     String encrypted = testing.encrypt(test);
    //     String decrypted = testing.decrypt(encrypted);
    //     System.out.println(encrypted);
    //     System.out.println(decrypted);
    
    
    // }
}


   