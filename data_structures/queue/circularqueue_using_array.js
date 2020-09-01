const input = require("prompt-sync")();

class circulerqueue{
	constructor(size =5){
		this.size = size;
		this.front = this.rear = -1;
		this.arr = new Array(size)
		console.log("queue is created of size "+size);
	}

	insertion(value){
		if(this.rear-this.front==this.size-1 || this.rear+1==this.front){
			console.log("queue is full");
			return 0;
		}
		else if(this.rear==-1){
			this.rear=this.front=0;
			this.arr[this.rear]=value;
		}
		else if(this.rear==this.size-1&&this.front>=0){
			this.rear=0;
			this.arr[this.rear]=value;
		}
		else{
			this.rear++;
			this.arr[this.rear]=value;
		}
		console.log(value+" is added in queue");
		console.log("front: ",this.front);
        console.log("rear: ",this.rear);
        return 1;
	}

	deletion(){
		var x =0;
		if(this.front==-1){
			console.log("queue is empty.");
			return x;
		}
		else if(this.front==this.size-1 && this.rear>=0){
			x = this.arr[this.front];
			this.front=0;
		}
		else if(this.rear==this.front){
			x = this.arr[this.front];
			this.front = this.rear = -1;
		}
		else{
			x = this.arr[this.front];
			this.front++;
		}	
		console.log(x+" is deleted from queue");
		console.log("front: ",this.front);
        console.log("rear: ",this.rear);
		return x;
	}
}




var size=input("enter the size of queue: ");
var qu = new circulerqueue(size);
console.log("1: insertion \n2: deletion \n3: display\n4: exit");
while(true){
    var x=input("enter choice: ");
    if(x==1){
        var value = Number(input("enter value: "));
        qu.insertion(value);
    }
    else if(x==2){
        qu.deletion();
    }
    else{
        break;
    }
}



