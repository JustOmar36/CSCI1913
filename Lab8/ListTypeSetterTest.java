
public class ListTypeSetterTest {
    public static void main(String[] args){
        ListTypeSetter test1 = new ListTypeSetter(1);
        System.out.println(test1.currentSize());//1
        test1.addToList("Skrr");
        System.out.println(test1.currentSize());//2
        System.out.println(test1.toString());//Skrr
        test1.addToList("Brr");
        System.out.println(test1.currentSize());//2
        System.out.println(test1.toString());//Skrr, Brr
        test1.reset();
        System.out.println(test1.currentSize()); //0
        System.out.println(test1.toString());//""





        ListTypeSetter test2 = new ListTypeSetter(2);
        ListTypeSetter test3 = new ListTypeSetter(3);
        ListTypeSetter test4 = new ListTypeSetter(3);
    }
}