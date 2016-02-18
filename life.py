import numpy as np
from Tkinter import *

def count_live(grid, point, radius=1, wrap=False):
    pad_mode = 'wrap' if wrap else 'constant'
    padded = np.pad(grid, radius, mode=pad_mode, constant_values=0)
    x, y = map(lambda a: a+1, point)
    return np.sum(padded[x-radius:x+radius+1, y-radius:y+radius+1]) - padded[x,y]

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
        self.rects = []
        self.size = 5
        self.delay = 10
        self.grid = np.random.randint(0, 2, size=(100,100))
        dim = self.grid.shape
        self.root = Tk()
        self.canvas = Canvas(self.root, width=dim[0]*self.size, height=dim[1]*self.size)
        self.canvas.pack()
        self.root.after(self.delay, self.step)
        self.root.mainloop()

    def step(self):
        size = self.size
        self.canvas.delete(ALL)
        self.new_rects = []
        for point in np.ndindex(self.grid.shape):
            if self.grid[point] == 1:
                x, y = point
                if len(self.rects) == 0:
                    r = self.canvas.create_rectangle(x*size, y*size, (x+1)*size, (y+1)*size, fill='black')
                else:
                    r = self.rects.pop()
                    c = np.array(self.canvas.coords(r)[:2])
                    nc = np.array([x*size, y*size])
                    offs = c - nc
                    c.move(r, offs[0], offs[1])
                self.new_rects.append(r)
        self.rects = self.new_rects
        self.grid = iterate(self.grid)
        self.root.update()
        self.root.after(self.delay, self.step) 

if __name__ == '__main__':
    anim = Animation()
