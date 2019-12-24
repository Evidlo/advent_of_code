// Evan Widloski - 2019-12-18
// Advent of Code - Day 2

package main

import (
	"fmt"
	"math"
)

// system state
type State struct {
	// program
	tape []int
	// pointer to current program address
	index int
	// program input stack
	input []int
	// program output stack
	output []int
}

// ----------------- operators ------------------

type Operation struct {
	// operation function
	function func(*State, []int)
	// number of operation parameters
	num_params int
	// which parameters are position mode by default (1-indexed)
	imm_mode []int
}

func add(s *State, params []int) {
	fmt.Printf("@ADD %d, %d -> *%d\n", params[0], params[1], params[2])

	s.tape[params[2]] = params[0] + params[1]
}

func mult(s *State, params []int) {
	fmt.Printf("@MULT %d, %d -> *%d\n", params[0], params[1], params[2])

	s.tape[params[2]] = params[0] * params[1]
}

// -------------- main program loop ---------------

func contains(arr []int, i int) bool {
	for _, n := range arr {
		if i == n {
			return true
		}
	}
	return false
}

func get_params(s *State, param_modes int, o Operation) []int {
	params := []int{}
	for p := 1; p <= o.num_params; p++ {
		place := int(math.Pow(10, float64(p)))

		if contains(o.imm_mode, p) || (param_modes/place)%place == 1 {
			// immediate mode
			params = append(params, s.tape[s.index+p])
		} else {
			// position mode
			params = append(params, s.tape[s.tape[s.index+p]])
		}
	}
	return params
}

func main() {
	operations := map[int]Operation{
		1: Operation{function: add, num_params: 3, imm_mode: []int{3}},
		2: Operation{function: mult, num_params: 3, imm_mode: []int{3}},
	}
	tape := []int{1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50}
	s := State{tape: tape, index: 0, input: []int{}, output: []int{}}

	for true {
		opcode, param_modes := s.tape[s.index]%100, s.tape[s.index]/100
		fmt.Println(s.tape)
		if opcode == 99 {
			break
		} else {
			o := operations[opcode]
			o.function(&s, get_params(&s, param_modes, o))
			s.index += o.num_params + 1
		}
	}
	fmt.Println(s.tape)
}
