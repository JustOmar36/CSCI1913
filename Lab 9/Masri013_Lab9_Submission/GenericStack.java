//Omar Masri - Masri013
public class GenericStack <Elem>{
    private Elem[] data;
    private int maxSize;
    private int count = 0;

    public GenericStack(int maxSize){
        this.maxSize = maxSize;
        data = (Elem[]) new Object[maxSize];
        }
    
    public boolean isEmpty(){
        if(count == 0){
            return true;
        }
        return false;
    }

    public void push(Elem x){
        if(count == data.length){
            Elem[] doubleSizeArray = (Elem[]) new Object[data.length * 2];
            for(int i = 0; i < data.length; i++){
                doubleSizeArray[i] = data[i];
            }
            data = doubleSizeArray;
        }
        data[count] = x;
        count++;
    }
    public Elem peek(){
        if(count == 0){
            return null;
        }
        return data[count - 1];
    }

    public Elem pop(){
        Elem returnedElement;
        if(count == 0){
            return null;
        }
        returnedElement = data[count - 1];
        data[count - 1] = null;
        count--;
        return returnedElement;
    }


}