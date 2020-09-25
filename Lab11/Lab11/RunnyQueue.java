
public class RunnyQueue<T>{
    private int count;
    private RunnyQueueNode<T> top;
    private RunnyQueueNode<T> head;
    
    public RunnyQueue(){
        top = null;
        head = null;
        count = 0;
    }

    public void enqueue(T x){
            if(top == x){
                count++;
            }
            else{
                RunnyQueueNode<T> newTop = new RunnyQueueNode<>(x, top);
                top = newTop;
                count++;
            }
        }
    
    public T front(){
        if(isEmpty() == true){
            return null;
        }
        return head.getData();
    }

    public int getSize(){
        return count;
    }

    public boolean isEmpty(){
        if(count == 0){
            return true;
        }
        return false;
    }
}