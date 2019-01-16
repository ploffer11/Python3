class Board:
    def __init__(self):
        self.n, self.m = (
            map(int, input().split())
        )
        self.ans = 64
        self.board = [input() for i in range(self.n)]

    def check(self, r, c):
        check1, check2 = 0, 0
        checkboard = ["W", "B"]
        for i in range(8):
            for j in range(8):
                check1 += (
                    self.board[r + i][c + j] == checkboard[(i+j) % 2]
                )
                check2 += (
                    self.board[r + i][c + j] == checkboard[(i+j+1) % 2]
                )
        self.ans = min(self.ans, 64-check1, 64-check2)

    def solve(self): 
        for i in range(self.n - 7):
            for j in range(self.m - 7):
                self.check(i, j)

board = Board()
board.solve()
print(board.ans)