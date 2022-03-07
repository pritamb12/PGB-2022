import util.fact;
public class maincode{
	public static void main(String[] args) {
		student stu1=new student();
		student stu2=new student();
		
		
		stu1.overload("nithish",2);
		stu1.overload("kumar",2,89);
		
		
		fact obj=new fact();
		System.out.println(obj.factorialrecursion(6));
		System.out.println(obj.factorial(5));
		
	}
}