package test;
import util.Factorial;
public class Main {
	public static void main(String[] args) {
		Employee e1 = new Employee(1,"Kumar","kumar@mail.com");
		Employee e2 = new Employee(1,"Kumar","kumar@mail.com");
		e1.display(1, "kumar");
		e2.display(1, "kumar","kumar@mail.com");
		System.out.println(e1.equals(e2));
		

		//Factorial 
		int n = 5;
		Factorial f = new Factorial();
		System.out.println("Using recursion: "+f.recursiveFunction(n));
		System.out.println("Without recursion: "+f.nonRecursiveFunction(n));
		

	}
}
