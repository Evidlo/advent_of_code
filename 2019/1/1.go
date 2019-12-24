package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	total := 0
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		for num > 0 {
			total += num
			num = int(num/3) - 2
		}
	}
	fmt.Println(total)
}
