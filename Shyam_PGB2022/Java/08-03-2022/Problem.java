import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.*;
import java.util.function.Supplier;
import java.util.function.Predicate;
import java.util.function.Consumer; 

interface Sayable{  
    void say();  
}  
public class Problem {
	static void printMessage(String name){  
        	System.out.println("Hello "+name);  
   	}  
   	public static void saySomething(){
   	 	System.out.println("HEYYY");
   	 }
	public static void main(String args[])
	{
		Sayable s = Problem::saySomething; //Method Reference
		s.say();
		Consumer<String> consumer = Problem::printMessage;  //Creating consumer
        	consumer.accept("SHYam");  
		Predicate<String> pr = message -> (message == "Hi"); // Creating predicate  
        	System.out.println(pr.test("Hey"));
		Supplier<Double> randomValue = () -> Math.random();// Creating Supplier
		System.out.println(randomValue.get());
		Integer a[]= {52,90,91,12,17,20,13,15,59,61};
		List<Integer> l=Arrays.asList(a);
		l.stream().map(n->n).forEach(System.out::println);
		l.stream().filter(p->validate(p) && p<25).forEach(System.out::println);
		List<Integer> prime = l.stream().filter(p->validate(p)).collect(Collectors.toList());
		List<Integer> show = prime.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
		System.out.println("The prime numbers in the input are:" +show);
		int add =l.stream().reduce(0,(ans,i)-> ans+i);
		System.out.println("Value after reduced is: "+add);	
	}
	private static Boolean validate(Integer p) {
		int n=(int)p;
		if(n<=1)return false;
		for(int i=2;i*i<=n;i++)
		{
			if(n%i==0)
				return false;
		}
		return true;	
	}
}
