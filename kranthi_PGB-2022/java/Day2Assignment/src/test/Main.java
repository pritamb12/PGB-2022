package test;
import util.Fact;

public class Main {
	public static void main(String args[]) {
		Student st1=new Student();
		Student st2=new Student();
		st1.override("kanthi", 3);
		st1.override("kanthi", 3,21);
		
		Fact f=new Fact();
		System.out.println(f.factorialrec(5));
		System.out.println(f.factorial(4));
		
		
	}

}
