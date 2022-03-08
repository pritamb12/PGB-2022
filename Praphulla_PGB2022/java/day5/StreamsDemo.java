import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.*;
import java.util.function.Supplier;
import java.util.function.Predicate;
import java.util.function.Consumer; 
 
public class StreamsDemo {
	public static void main(String args[])
	{
		Integer a[]= {55,96,65,61,53,20,13,11,5,93};
		List<Integer> l=Arrays.asList(a);
		System.out.println("Printing Prime and Composite numbers(using map):");
		l.stream().map(n->n).forEach(System.out::println);
		System.out.println("The Primes less than 25 are(using filter):");
		l.stream().filter(p->validate(p) && p<25).forEach(System.out::println);
		List<Integer> prime = l.stream().filter(p->validate(p)).collect(Collectors.toList());
		List<Integer> show = prime.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
		System.out.println("The prime numbers in the given input are(using sort):" +show);
		int add =l.stream().reduce(0,(ans,i)-> ans+i);
		System.out.println("The reduced value is(using reduce): "+add);	
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
