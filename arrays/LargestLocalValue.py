def LargestLocal(grid:list[list[int]])->list[list[int]]:
    N = len(grid)
    ans = [[0] * (N-2) for _ in range(N-2)]
    for i in range(N-2):
        for j in range(N-2):
            ans[i][j] = grid[i][j]
            for di in range(3):
                for dj in range(3):
                    ans[i][j] = max(ans[i][j],grid[i+di][j+dj])
    return ans
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(LargestLocal(grid))