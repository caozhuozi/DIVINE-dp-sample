import sys

def min_cost(N, p, dp, mem):
    for i in reversed(range(0, N)):
        for j in range(1, N+1):
            min_ = ((N-i)/N) * (j ** p)
            mem[i][j] = j
            for k in range(i+1, j):
                if dp[i][k] + dp[k][j] < min_:
                    min_ = dp[i][k] + dp[k][j]
                    mem[i][j] = k
            dp[i][j] = min_
    return dp[0][N]


def get_sequence_points(res, mem, start, end):
    if start >= end or start == -1 or end == -1:
        return
    t = mem[start][end]
    if t == start or t == end:
        return
    res.add(mem[start][end])
    get_sequence_points(res, mem, start, t-1)
    get_sequence_points(res, mem, t+1, end)


if __name__ == "__main__":
    N_, p_ = int(sys.argv[1]), float(sys.argv[2])
    # N_ = 1200
    # p_ = 1.5
    dp_ = [[0] * (N_ + 1) for i in range(N_ + 1)]
    mem_ = [[0] * (N_ + 1) for i in range(N_ + 1)]
    m_c = min_cost(N_, p_, dp_, mem_)
    print(
        "the minimum cost is:", m_c
    )
    seqs = {0, N_}
    get_sequence_points(seqs, mem_, 0, N_)
    seqs = sorted(seqs)
    print(
        "the generated sequence is:", seqs
    )