
public class RunnyQueueNode<T> {
    private T data;
    private int count;
    private RunnyQueueNode<T> next;

    public RunnyQueueNode(T data){
        this(data, null);
    }
    
    public RunnyQueueNode(T data, RunnyQueueNode<T> next){
        this.data = data;
        this.next  = next;
        count = 1;
    }
    
    public T getData(){
        return data;
    }

    public int getCount(){
        return count;
    }

    public RunnyQueueNode<T> getNext(){
        return next;
    }

    public void setData(T data){
        this.data = data;
    }

    public void setCount(int count){
        this.count = count;
    }

    public void setNext(RunnyQueueNode<T> next){
        this.next = next;
    }
}