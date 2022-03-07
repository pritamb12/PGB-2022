class genericdata<T> {

    private T data;
    genericdata(T obj) { this.data = obj; }
    public void display() { System.out.println(this.data); }
}
  
class generic {
    public static void main(String[] args){
        genericdata<Integer> obj1 = new genericdata<Integer>(150);
        genericdata<String> obj2 = new genericdata<String>("string");
        obj1.display();
        obj2.display();
    }
}