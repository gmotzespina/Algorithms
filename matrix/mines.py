from collections import deque 

class MineSweeper:

    def __init__(self, size: (int, int)):
        self.size = size 
        rows, cols = self.size
        self.matrix = [[0 for i in range(cols)] for i in range(rows)] 

    def print_matrix(self):
        list_rows = []
        for row in self.matrix:
            list_rows.append(str(row))
        print('[' + ',\n '.join(list_rows) + ']')
        print()

    def build_matrix(self, bombs: [[int]]):
        rows, cols = self.size
        for bomb in bombs:
            x, y = bomb
            self.matrix[x][y] = -1
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if j >= 0 and j < rows:
                        if i >= 0 and i < cols:
                            if self.matrix[i][j] != -1:
                                self.matrix[i][j] += 1

    def expand(self, click_coords):

        rows, cols = self.size
        x, y = click_coords
        zeros_queue = deque()
        
        if self.matrix[x][y] == 0:
            zeros_queue.append(click_coords)
            self.matrix[x][y] = -2

        while len(zeros_queue) > 0:
            x, y = zeros_queue[0]
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if j >= 0 and j < rows:
                        if i >= 0 and i < cols:
                            if self.matrix[i][j] == 0:
                                zeros_queue.append([i, j])
                                self.matrix[i][j] = -2

            zeros_queue.popleft()

mine_sweeper = MineSweeper((10,10))

mine_sweeper.print_matrix()

mine_sweeper.build_matrix(bombs=[[1,1], [5,5], [8,3], [3,3], [3,4],[4,5], [1,2], [6,8]])

mine_sweeper.print_matrix()

mine_sweeper.expand([4,0])

mine_sweeper.print_matrix()

mine_sweeper.expand([0,2])

mine_sweeper.print_matrix()

