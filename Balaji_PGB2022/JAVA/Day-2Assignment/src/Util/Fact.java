package Util;

public class Fact {
	
		public int non_recursive(int num)
		{
			int fact=1;
			for(int i=1;i<=num;i++)
			{
				fact*=i;
			}
			return fact;
		}
		public int recursive(int n)
		{
			if(n==1) return 1;
			else
				return(n*recursive(n-1));
		}
	}

