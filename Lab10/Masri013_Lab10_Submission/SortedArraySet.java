import java.util.Arrays;

public class SortedArraySet<T extends Comparable<? super T>> {
    // There is a fair amount of code being provided for this class. Most of this is stuff that you would already had
    // access to from class slides or code posted with the slides. Some of it is updated/upgraded from what we saw in
    // class and a tiny amount of it is the consequence of code interactions we havn't been able to discuss.

    private T[] data;
    private int size;

    public SortedArraySet(int initialMax) {
        // Provided -- this one can be a bit tricky due to the silly type casting thing again
        // Because of the T extends Comparable<? super T> we have to use Comparable here not Object.
        data = (T[]) new Comparable[initialMax];
        this.size = 0;
    }

    /**
     * Shift the elements of the array starting at a point to the left
     * The element in position endingAt will be deleted overwritten by what used to be left of it
     * This will run through size (not the end of the array)
     * This will set the old "end of array" to be null.
     * This will update size.
     * @param endingAt
     */
    private void shiftLeft(int endingAt) {
        // This is an updated version that definitely won't out-of-bounds access
        // so long as size <= data.length(which should be true anyways)
        for(int i = endingAt+1; i < size; i++) {
            data[i-1] = data[i];
        }
        size--;
        data[size] = null;
    }

    /**
     * Shift the elements of the array starting at a point to the right
     * The element in position startingAt will be copied appearing both at startingAt and one to the right.
     * This will run through size (not the end of the array)
     * This will update size.
     * @param startingAt
     */
    private void shiftRight(int startingAt) {
        // This is an updated version that definitely won't out-of-bounds access
        // so long as size <= data.length(which should be true anyways)
        for (int i = size-1; i >= startingAt; i--) {
            data[i+1] = data[i];
        }
        size++;
        // this just effectively added something... better fix size.
    }

    // This one is provided because It's pretty specific and just for testing right now.
    @Override
    public String toString() {
        return Arrays.toString(data)+": "+ getSize();
    }

    // and I've given you this template because not writing this function will make this program SUCK
    private int find(T elem) {
        int low = 0;
        int high = size - 1;
        int mid;
        if (this.isEmpty() == true){
            return -1;
        }
        while (high >= low){
            mid = (high + low)/2;
                if(data[mid].compareTo(elem) < 0 ){
                    low = mid + 1;
                }
                else if(data[mid].compareTo(elem) > 0){
                    high = mid - 1;
                }
                else{
                    return mid;
                }
            }
            return -1;
    }

    public int getSize(){
        return size;
    }

    public boolean isEmpty(){
        if(size == 0){
            return true;
        }
        return false;
    }

    public boolean contains(T elem){
        if(this.find(elem) != -1) {
            return true;
        }
        return false;
    }

    public void add(T elem){
        if(this.contains(elem) == false){
            if(size == data.length){
                T[] newArray = (T[]) new Comparable [size * 2];
                for(int j = 0; j < size; j++){
                    newArray[j] = data[j];
                }
                data = newArray;
            }
            if(this.isEmpty() == true){
                data[size] = elem;
                size++;
            }
            if (data[size - 1].compareTo(elem) < 0){
                data[size] = elem;
                size++;
            }
            if(data[0].compareTo(elem) > 0){
                shiftRight(0);             
                data[0] = elem;
            }
            else{
                for(int i = 0; i < size; i++){
                    if((data[i].compareTo(elem) < 0 && data[i + 1].compareTo(elem) > 0)){
                        shiftRight(i);
                        if(size == data.length){
                            T[] newArray = (T[]) new Comparable [size * 2];
                            for(int j = 0; j < size; j++){
                                newArray[j] = data[j];
                            }
                            data = newArray;
                            break;
                        }
                        data[i + 1] = elem; 
                    }
                }
            }
        }
    }//add

    public void remove(T elem){
        if(this.contains(elem) == true){
            shiftLeft(this.find(elem));
        }
    }

    public T getSmallest(){
        return data[0];
    }

    public T getBiggest(){
        if (size == 0){
            return data[0];
        }
        return data[size -1];
    }
}


