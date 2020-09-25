import java.util.StringJoiner;

public class Dog implements Comparable<Dog>{

    public String name;
    public int age;
    public double weight;

    public Dog(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void celebrateBirthday() {
        age = age + 1;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    @Override
    public int compareTo(Dog other){
        if (this.getName().compareTo(other.getName()) < 0){
            return -1;
        }
        else if (this.getName().compareTo(other.getName()) > 0){
            return 1;
        }
        if(this.getName().compareTo(other.getName()) == 0){
            if(this.getAge() > other.getAge()){
                return 1;
            }
            else if (this.getAge() < other.getAge()){
                return -1;
            }
        }
        return 0;
    }
}
