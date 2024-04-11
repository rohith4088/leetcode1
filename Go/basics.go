package main
import (
	"fmt"
	//"go/types"
)

//import "time"

// func somefunc(num string) {
// 	fmt.Println(num)
// }
// func main() {
// 	go somefunc("1")
// 	go somefunc("2")
// 	go somefunc("3") // go routine --> running function concurrently
// 	//the results are frandom because all the functions are running asynchornously and the main function is not waiting for them to finish.
// 	//time.Sleep(time.Second * 2) // this is a hack to wait for the go routines to finish
// 	time.Sleep(time.Second * 2)
// 	fmt.Println("hi")
// }

// channels in go
// func main() {
// 	mychannel := make(chan string) // creating a channel
// 	go func() { // anonymous function
// 		mychannel <- "hello"
// 	}() // this is a go routine that is sending a message to the channel
// 	msg := <-mychannel // this is a blocking call
// 	fmt.Println((msg))
// this implements the joining point for the forked child process

//}

// Generics in go
func Add [t int | float64] (a t , b t) t{
	return (a + b)
}
func main(){
	result := Add(1,2)
	fmt.Println((result))

}
