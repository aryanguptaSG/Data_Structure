#include <stdio.h>
#include <stdlib.h>

struct queue
{int size,front,rear,*Q;};

void creatqueue(struct queue *qu){
	printf("\nenter the size of queue: ");
	scanf("%d",&qu->size);
	qu->front=0;
	qu->rear=-1;
	qu->Q=(int *)malloc(qu->size*sizeof(int));
}

void push(struct queue *qu,int value){
	if(qu->rear==qu->size-1){
		printf("\nqueue is full");
	}
	else{
		qu->rear++;
		qu->Q[qu->rear]=value;
		printf("%d id added in queue\n",value);
		printf("\nfront : %d  rear: %d\n",qu->front,qu->rear);
	}
}

int pop(struct queue *qu){
	int x=0;
	if(qu->front>qu->rear){
		printf("\nqueue is empty");
	}
	else{
		x=qu->Q[qu->front];
		printf("\n%d is poped\n", qu->Q[qu->front]);
		qu->front++;
		
	}
	return x;

}

void display(struct queue *qu){
	for(int i=qu->front;i<=qu->rear;i++){
		printf("%d\n", qu->Q[i]);
	}
}

int main()
{
	struct queue qu;
	creatqueue(&qu);
	while(1){
		printf("\npress 1 for push\npress 2 for pop\npress 3 for display\npress 4 for exit\nenter choice: ");
		int i;
		scanf("%d",&i);
		if (i==1)
		{
			int value;
			printf("enter the value: ");
			scanf("%d",&value);
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
