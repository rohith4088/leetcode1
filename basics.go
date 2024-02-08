package main

import "fmt"
import "time"

func somefunc(num string) {
	fmt.Println(num)
}
func main() {
	go somefunc("1")
	go somefunc("2")
	go somefunc("3") // go routine --> running function concurrently
	//the results are frandom because all the functions are running asynchornously and the main function is not waiting for them to finish.
	//time.Sleep(time.Second * 2) // this is a hack to wait for the go routines to finish
	time.Sleep(time.Second * 2)
	fmt.Println("hi")
}
