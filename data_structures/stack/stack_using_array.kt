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
}




fun main(args: Array<String>) {
    val x = readLine()
  
    
   
}