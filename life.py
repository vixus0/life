import numpy as np
from Tkinter import *

def count_live(grid, point, radius=1, wrap=False):
    x, y = point
    xslice = slice(max(0, x-radius), min(grid.shape[0], x+radius+1))
    yslice = slice(max(0, y-radius), min(grid.shape[1], y+radius+1))
    return np.sum(grid[xslice, yslice]) - grid[x,y]

def count_grid(grid):
    neighbours = np.zeros(grid.shape)
    for point in np.ndindex(grid.shape):
        neighbours[point] = count_live(grid, point)
    return neighbours

def iterate(start):
    end = start
    nb = count_grid(start)
    end[nb < 2] = 0
    end[nb > 3] = 0
    end[nb == 3] = 1
    return end

class Animation(object):
    def __init__(self):
        self.colors = {1:'black', 0:'white'}
        self.rects = {}
        self.size = 4
        self.delay = 0
        self.grid = np.random.randint(0, 2, size=(50,50))
        dim = self.grid.shape
        self.root = Tk()
        self.canvas = Canvas(self.root, width=dim[0]*self.size, height=dim[1]*self.size)
        self.init_rects()
        self.canvas.pack()
        self.root.after(self.delay, self.step)
        self.root.mainloop()

    def init_rects(self):
        for point in np.ndindex(self.grid.shape):
            x, y = point
            coords = (x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size)
            self.rects[point] = self.canvas.create_rectangle(
                    *coords, fill='white', width=0
                    )

    def step(self):
        size = self.size
        for point in np.ndindex(self.grid.shape):
            self.canvas.itemconfig(self.rects[point], fill=self.colors[self.grid[point]])
        self.grid = iterate(self.grid)
        self.root.update()
        self.root.after(self.delay, self.step) 

if __name__ == '__main__':
    anim = Animation()
