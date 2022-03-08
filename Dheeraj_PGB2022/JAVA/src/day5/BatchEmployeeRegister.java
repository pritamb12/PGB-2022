package day5;
import day3.*;

import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class EmpReg implements Runnable{
	
	int Id;
	String grp;
	List<String> givenList = Arrays.asList("A","B","C","D","E","F");
	
    public EmpReg(int id) {
        this.Id = id;
    } 
	
    // Defining Run for Runnable Interface
	public void run() {
		Random rand = new Random();
		// Use Thread Pool to Register Employees and assign them to Different Groups
		for (int i = Id;i < Id+10;i++ ) {
			grp = givenList.get(rand.nextInt(givenList.size()));
			Training.assign_to_group(grp, i,"Employee"+i);
			// System.out.println(Training.Groups.get(grp).size());
		}
	}
	

}

public class BatchEmployeeRegister{
	
	static final int max_threads = 10;
	
	public static void main(String[] args) throws InterruptedException {
		
        Runnable r1 = new EmpReg(1001);
        Runnable r2 = new EmpReg(1011);    
        Runnable r3 = new EmpReg(1021);
          
        // Create a Thread Pool With max 10 Threads
        ExecutorService pool = Executors.newFixedThreadPool(max_threads);  
         
        // Create Multiple Threads To Register Employees
        pool.execute(r1);
        pool.execute(r2);
        pool.execute(r3);
        
        // ThreadPool ShutDown
        pool.shutdown();  
        
        // Sleep to Update the Groups List
        Thread.sleep(10);
        
        // Print The Updated Employees Data after Using ThreadPool
        Training.print_group_data();
	}
}
