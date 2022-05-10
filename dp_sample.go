package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

func minCost(N int, p float64, dp [][]float64, mem [][]int) float64 {
	for i := N-1; i >= 0; i-- {
		for j := 1; j <= N; j++ {
			min_ := float64(N-i)/float64(N) * math.Pow(float64(j), p)
			mem[i][j] = j
			for k := i+1; k < j; k++ {
				if dp[i][k] + dp[k][j] < min_ {
					min_ = dp[i][k] + dp[k][j]
					mem[i][j] = k
				}
			}
			dp[i][j] = min_
		}
	}
	return dp[0][N]
}

func getSequencePoints(res map[int]bool, mem [][]int, start int, end int)  {
	if start >= end || start == -1 || end == -1 {
		return
	}
	t := mem[start][end]
	if t == start || t == end {
		return
	}
	res[t] = true
	getSequencePoints(res, mem, start, t-1)
	getSequencePoints(res, mem, t+1, end)
}

func main() {
	//N_:= 1000
	//p_ := 1.2
	N_, _:= strconv.Atoi(os.Args[1])
	p_, _:= strconv.ParseFloat(os.Args[2], 64)


	dp_ := make([][]float64,  N_+1)
	for i := range dp_ {
		dp_[i] = make([]float64, N_ + 1)
	}
	mem_ := make([][]int,  N_+1)
	for i := range mem_ {
		mem_[i] = make([]int, N_+1)
	}
	mC := minCost(N_, p_, dp_, mem_)
	res := make(map[int]bool)
	res[0] = true
	res[N_] = true
	getSequencePoints(res, mem_, 0, N_)
	fmt.Printf("the minimum cost is: %f\n", mC)
	var seqs []int
	for k := range res {
		seqs = append(seqs, k)
	}
	sort.Sort(sort.IntSlice(seqs))
	fmt.Println("the generated sequence is: ", seqs)
}
