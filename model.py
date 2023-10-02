class LifeGame:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = [[0 for i in range(width)] for j in range(height)]

    def randlife(self):
        import random
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.map[y][x] = random.randint(0, 1)

    def load_map(self, map,x=75,y=75):
        for i in range(0,len(map)):
            for k in range(0,len(map[i])):
                self.map[x+k][y+i] = map[i][k]

    def clear_map(self):
        self.map = [[0 for i in range(self.width)] for j in range(self.height)]

    def gen_next(self):
        temp = [[0 for i in range(self.width)] for j in range(self.height)]
        for y in range(0, self.height):
            for x in range(0,self.width):
                temp[y][x] = self.map[y][x]
        for y in range(0, self.height):
            for x in range(0, self.width):
                cell = self.map[y][x]
                count = self.count_neighbors(x, y)
                if cell == 1:
                    if count < 2:
                        temp[y][x] = 0
                    elif count > 3:
                        temp[y][x] = 0
                if cell == 0:
                    if count == 3:
                        temp[y][x] = 1
        self.map = temp

    def count_neighbors(self, x, y):
        count = 0
        if y-1 >= 0:
            count += self.map[y-1][x]
        if y-1 >= 0 and x-1 >= 0:
            count += self.map[y-1][x-1]
        if y-1 >= 0 and x+1 < self.width:
            count += self.map[y-1][x+1]
        if x-1 >= 0:
            count += self.map[y][x-1]
        if x+1 < self.width:
            count += self.map[y][x+1]
        if y+1 < self.height:
            count += self.map[y+1][x]
        if y+1 < self.height and x-1 >= 0:
            count += self.map[y+1][x-1]
        if y+1 < self.height and x+1 < self.width:
            count += self.map[y+1][x+1]
        return count
