const input = require("prompt-sync")();
 
class queue{
    constructor(size=5){
        this.size=size;
        this.front=0;
        this.rear=-1;
        this.array= new Array(size);
    }
    push(value){
        if(this.rear==this.size-1){
            console.log("queue is full");
            return 0;
        }
        else{
            this.rear++;
            this.array[this.rear]=value;
            console.log(value, " is added in queue");
            console.log("front: ",this.front);
            console.log("rear: ",this.rear);
            return 1;
        }
    }
    pop(){
        if(this.front>this.rear){
            console.log("queue is empty");
            return 0;
        }
        else{
            console.log(this.array[this.front], " is poped");
            this.front++;
            console.log("front: ",this.front);
            console.log("rear: ",this.rear);
            return 1;

        }
    }

    display(){
        if(this.front>this.rear){
            console.log("queue is empty");
            return 0;
        }
        else{
            for(var i=this.front;i<=this.rear;i++){
                console.log(this.array[i]);
            }
        }
    }
}


var qu =new queue();
console.log("1: push \n2: pop \n3: display\n4: exit");
while(true){
    var x=input("enter choice: ");
    if(x==1){
        var value = Number(input("enter value: "));
        qu.push(value);
    }
    else if(x==2){
        qu.pop();
    }
    else if(x==3){
        qu.display();
    }
    else{
        break;
    }
}
