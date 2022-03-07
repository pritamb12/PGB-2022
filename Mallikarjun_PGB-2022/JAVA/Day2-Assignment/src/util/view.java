package util;

public class view<T> {
	private T d;
	public void addData(T d) {
		this.d = d;
	}
	public T getData() {
		return d;
	}
	public static void main(String[] args) {
		view<Integer> integer = new view<Integer>();
		view<String> String = new view<String>();
		
		integer.addData(10);
		String.addData("This is a String");
		
		System.out.println(integer.getData());
		System.out.println(String.getData());
		
	}

}
