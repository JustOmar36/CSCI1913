import java.util.Random;
import java.util.StringJoiner;

public class Cat implements Comparable<Cat> {

    public String name;
    public int age;
    public double weight;

    public Cat(String name, int age, double weight) {
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
    public int compareTo(Cat other) {
        // TODO: write this function
        if(this.getAge() > other.getAge()){
            return 1;
        }
        else if(this.getAge() < other.getAge()){
            return -1;
        }
        else if (this.getAge() == other.getAge()){
            if(this.getWeight() > other.getWeight()){
                return 1;
            }
            else if (this.getWeight() < other.getWeight()){
                return -1;
            }
        }
            return 0;
    }
}
