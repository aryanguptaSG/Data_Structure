class stack(_size : Int =5){
    var size: Int
    var top: Int
    var arr = IntArray(_size)
    
    init{
        size = _size
        top=-1
        println("stack created of $size")
    }
    
    fun push(value:Int){
        if(top==size-1){
            println("stack overflow")
        }
        else{
            top++
            arr[top]=value
            println("$value is added in stack")
        }
    }
    fun pop(){
        if (top==-1){
            println("stack is underflow")
        }
        else{
            var x =arr[top]
            println("$x is poped")
            top--
        }
    }
    fun display(){
        if (top==-1){
            println("stack is underflow")
        }
        else{
            var i = top
            while(i>=0){
                println(arr[i])
                i--
            }
        }

    }
}




fun main(args: Array<String>) {
    print("enter the size of stack: ")
    val size = Integer.parseInt(readLine())
    val st = stack(size)
    println("enter 1 for push\nenter 2 for pop\nenter 3 for display\nenter 4 for exit")
    while(true){
        print("enter choice: ")
        var x =Integer.parseInt(readLine())
        when(x){
            1->{
                print("enter value: ")
                var value =Integer.parseInt(readLine())
                st.push(value)
            }
            2->st.pop()
            3->st.display()
            else->break
        }
    }
  
    
   
}