package main

import (
	"bufio"
	"log"
	"os"
	"sort"
	"strconv"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	numbers := []int{}
	for scanner.Scan() {
		text := scanner.Text()
		num, e := strconv.Atoi(text)
		if e != nil {
			log.Println("Unparseable line: " + text)
			continue
		}
		numbers = append(numbers, num)
	}
	if err = scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// puzzle1(numbers)
	puzzle2(numbers)
}

func puzzle1(numbers []int) {
	sort.Ints(numbers)
	log.Printf("%v numbers total\n", len(numbers))
	for _, n := range numbers {
		matchFinder := func(j int) bool {
			sum := numbers[j] + n
			// log.Printf("Searching %v, index %v (value %v) yields sum %v\n", n, j, numbers[j], sum)
			isPotentialMatch := sum >= 2020
			return isPotentialMatch
		}
		indexMatch := sort.Search(len(numbers), matchFinder)
		if indexMatch < len(numbers) && numbers[indexMatch]+n == 2020 {
			log.Println("Found 2020 sum pair!")
			log.Println(n)
			log.Println(numbers[indexMatch])
		} else {
			// log.Printf("No match. Searched %v and indexMatch was %v\n", n, indexMatch)
			continue
		}
	}
}

func puzzle2(numbers []int) {
	sort.Ints(numbers)
	for _, n := range numbers {
		for _, m := range numbers {
			matchFinder := func(j int) bool {
				sum := numbers[j] + n + m
				// log.Printf("Searching %v, index %v (value %v) yields sum %v\n", n, j, numbers[j], sum)
				isPotentialMatch := sum >= 2020
				return isPotentialMatch
			}
			indexMatch := sort.Search(len(numbers), matchFinder)
			if indexMatch < len(numbers) && numbers[indexMatch]+n+m == 2020 {
				log.Println("Found 2020 sum pair!")
				log.Println(n)
				log.Println(m)
				log.Println(numbers[indexMatch])
			}
		}
	}
}
