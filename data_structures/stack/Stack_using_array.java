public class Stack{
	int size=5,top=-1;
	int arr[]=new int[size];

	public void push(int value){
		if(top==size-1){
			System.out.println("Stack Overflow.");
		}
		else{
			top++;
			arr[top]=value;
			System.out.println(value+" is added in stack"+"  top is: "+top);
		}
	}

	public int pop(){
		int x=0;
		if(top==-1){
			System.out.println("Stack Underflow.");
			return x;
		}
		else{
			x=arr[top];
			System.out.println(x+" is removed from stack");
			top--;
			System.out.println("top is: "+top);
			return x;
		}
	}

	public void display(){
		if(top==-1){
			System.out.println("Stack is empty.");
		}
		else{
			for(int i=top;i>=0;i--)
			{
			System.out.println(arr[i]);
		}
		}
	}

	public static void main(String[] args) {
		Stack st = new Stack();
		st.push(5);
		st.push(6);
		st.push(7);
		st.display();
		st.pop();
		st.display();
		st.push(8);
		st.push(9);
		st.push(10);
		st.display();
		st.pop();
		st.pop();
		st.pop();
		st.display();
		st.pop();
		st.pop();
		st.pop();
		st.display();
	}
}