#include <iostream>
using namespace std;
struct queue{
	int size,front,rear,*Q;
};

void creatqueue(struct queue *qu){
	cout<<"\nenter the size of queue: ";
	cin>>qu->size;
	qu->front=qu->rear=-1;
	qu->Q=new int[qu->size];
}

int push(struct queue *qu,int value){
	if(qu->rear-qu->front==qu->size-1 || qu->rear+1==qu->front){
		cout<<"\nqueue is full";
		cout<<"\nfront : "<<qu->front;
		cout<<"\nrear: "<<qu->rear;
		return 0;
	}
	else if(qu->rear==-1){
		qu->rear=qu->front=0;
		qu->Q[qu->rear]=value;
	}
	else if(qu->rear==qu->size-1 && qu->front>=0){
		qu->rear=0;
		qu->Q[qu->rear]=value;
	}
	else{
		qu->rear++;
		qu->Q[qu->rear]=value;
	}
	cout<<"\n"<<value<<" is added in queue";
	cout<<"\nfront : "<<qu->front;
	cout<<"\nrear: "<<qu->rear;
	return value;
}

int pop(struct queue *qu){
	int x=0;
	if(qu->front==-1){
		cout<<"\nqueue is empty";
		return x;
	}
	else if(qu->front==qu->rear){
		x=qu->Q[qu->front];
		qu->front=qu->rear=-1;
	}
	else if(qu->front==qu->size-1&&qu->rear>=0){
		x=qu->Q[qu->front];
		qu->front=0;
	}
	else{
		x=qu->Q[qu->front];
		qu->front++;

	}
	cout<<"\n"<<x<<" is poped";
	cout<<"\nfront : "<<qu->front;
	cout<<"\nrear: "<<qu->rear;
	return x;

}

void display(struct queue *qu){
	if(qu->front==-1){
		cout<<"\nqueue is empty";
	}
	else if(qu->rear>=qu->front){
		for(int i=qu->front;i<=qu->rear;i++){
		cout<<"\n"<<qu->Q[i];
	}
	}
	else{
		for(int i=qu->front;i<=qu->size-1;i++){
		cout<<"\n"<<qu->Q[i];}
		for(int i=0;i<=qu->rear;i++){
		cout<<"\n"<<qu->Q[i];
	}

	}

}

int main()
{
	struct queue qu;
	creatqueue(&qu);
	cout<<"\npress 1 for push\npress 2 for pop\npress 3 for display\npress 4 for exit\n";
	while(true){
		cout<<"\nenter choice: ";
		int i;
		cin>>i;
		if (i==1)
		{
			int value;
			cout<<"enter the value: ";
			cin>>value;
			push(&qu,value);
		}
		else if (i==2)
		{
			pop(&qu);
		}
		else if (i==3)
		{
			display(&qu);
		}
		else
		{
			break;
		}
	}
	return 0;
}



