public class mainclass{
		public static void main(String[] args) {
			System.out.println("enter the size of queue: ");
			linearqueue qu =new linearqueue();
			System.out.println(qu.size);

		}
	}

class linearqueue{
		int top =-1,size = 5;
		int queue[]=new int[size];

}