
public class BraceChecker {
    public static boolean checkBraces(String x){
        GenericStack stack = new GenericStack<>(5);
        for(int i = 0; i < x.length(); i++){
            if(x.charAt(i) == '(' || x.charAt(i) == '[' || x.charAt(i) == '{'){
                stack.push(x.charAt(i));
            }

            else if (stack.isEmpty() == true){
                if(x.charAt(i) == ')' || x.charAt(i) == ']' || x.charAt(i) == '}')
                return false;
            }

            else if (x.charAt(i) == ')' && stack.peek() == (Character)'(' || x.charAt(i) == ']' && stack.peek() == (Character)'[' || x.charAt(i) == '}' && stack.peek() == (Character)'{'){
                stack.pop();
            }
        }
        if(stack.isEmpty() == true){
            return true;
        }
        else{
            return false;
        }
    }


}