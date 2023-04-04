"""
Reinforcement learning black white chess board robot occupation game.

Red rectangle:          explorers(two robots).
Black rectangles:       black obstructions         [reward = -10].
yellow rectangles:      yellow obstructions        [reward = -10].
All other states:       ground                     [reward = 8/-10 (robots is encountered?)].

"""


import numpy as np
import time
import sys
# check python version
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 40   # pixels
MAZE_H = 5  # grid height
MAZE_W = 16  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['1u2u', '1u2d', '1d2u', '1d2d']
        self.n_actions = len(self.action_space)
        self.title('chess board')
        self.geometry('{0}x{1}'.format(MAZE_W * UNIT, MAZE_H * UNIT))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        refer = np.array([20, 20])
        origin1 = refer + np.array([UNIT * 0, UNIT * 1])
        origin2 = refer + np.array([UNIT * 0, UNIT * 3])

        # create rectangle, black rectangle obstructions
        self.black_rect = []
        # black rect 1
        black_rect_center1 = refer + np.array([UNIT * 4, UNIT * 0])
        black_rect1 = self.canvas.create_rectangle(
            black_rect_center1[0] - 15, black_rect_center1[1] - 15,
            black_rect_center1[0] + 15, black_rect_center1[1] + 15,
            fill='black')
        self.black_rect.append(black_rect1)
        # black rect 2
        black_rect_center2 = refer + np.array([UNIT * 8, UNIT * 0])
        black_rect2 = self.canvas.create_rectangle(
            black_rect_center2[0] - 15, black_rect_center2[1] - 15,
            black_rect_center2[0] + 15, black_rect_center2[1] + 15,
            fill='black')
        self.black_rect.append(black_rect2)
        # black rect 3
        black_rect_center3 = refer + np.array([UNIT * 10, UNIT * 0])
        black_rect3 = self.canvas.create_rectangle(
            black_rect_center3[0] - 15, black_rect_center3[1] - 15,
            black_rect_center3[0] + 15, black_rect_center3[1] + 15,
            fill='black')
        self.black_rect.append(black_rect3)
        # black rect 4
        black_rect_center4 = refer + np.array([UNIT * 14, UNIT * 0])
        black_rect4 = self.canvas.create_rectangle(
            black_rect_center4[0] - 15, black_rect_center4[1] - 15,
            black_rect_center4[0] + 15, black_rect_center4[1] + 15,
            fill='black')
        self.black_rect.append(black_rect4)
        # black rect 5
        black_rect_center5 = refer + np.array([UNIT * 1, UNIT * 1])
        black_rect5 = self.canvas.create_rectangle(
            black_rect_center5[0] - 15, black_rect_center5[1] - 15,
            black_rect_center5[0] + 15, black_rect_center5[1] + 15,
            fill='black')
        self.black_rect.append(black_rect5)
        # black rect 6
        black_rect_center6 = refer + np.array([UNIT * 5, UNIT * 1])
        black_rect6 = self.canvas.create_rectangle(
            black_rect_center6[0] - 15, black_rect_center6[1] - 15,
            black_rect_center6[0] + 15, black_rect_center6[1] + 15,
            fill='black')
        self.black_rect.append(black_rect6)
        # black rect 7
        black_rect_center7 = refer + np.array([UNIT * 11, UNIT * 1])
        black_rect7 = self.canvas.create_rectangle(
            black_rect_center7[0] - 15, black_rect_center7[1] - 15,
            black_rect_center7[0] + 15, black_rect_center7[1] + 15,
            fill='black')
        self.black_rect.append(black_rect7)
        # black rect 8
        black_rect_center8 = refer + np.array([UNIT * 2, UNIT * 2])
        black_rect8 = self.canvas.create_rectangle(
            black_rect_center8[0] - 15, black_rect_center8[1] - 15,
            black_rect_center8[0] + 15, black_rect_center8[1] + 15,
            fill='black')
        self.black_rect.append(black_rect8)
        # black rect 9
        black_rect_center9 = refer + np.array([UNIT * 6, UNIT * 2])
        black_rect9 = self.canvas.create_rectangle(
            black_rect_center9[0] - 15, black_rect_center9[1] - 15,
            black_rect_center9[0] + 15, black_rect_center9[1] + 15,
            fill='black')
        self.black_rect.append(black_rect9)
        # black rect 10
        black_rect_center10 = refer + np.array([UNIT * 8, UNIT * 2])
        black_rect10 = self.canvas.create_rectangle(
            black_rect_center10[0] - 15, black_rect_center10[1] - 15,
            black_rect_center10[0] + 15, black_rect_center10[1] + 15,
            fill='black')
        self.black_rect.append(black_rect10)
        # black rect 11
        black_rect_center11 = refer + np.array([UNIT * 10, UNIT * 2])
        black_rect11 = self.canvas.create_rectangle(
            black_rect_center11[0] - 15, black_rect_center11[1] - 15,
            black_rect_center11[0] + 15, black_rect_center11[1] + 15,
            fill='black')
        self.black_rect.append(black_rect11)
        # black rect 12
        black_rect_center12 = refer + np.array([UNIT * 12, UNIT * 2])
        black_rect12 = self.canvas.create_rectangle(
            black_rect_center12[0] - 15, black_rect_center12[1] - 15,
            black_rect_center12[0] + 15, black_rect_center12[1] + 15,
            fill='black')
        self.black_rect.append(black_rect12)
        # black rect 13
        black_rect_center13 = refer + np.array([UNIT * 14, UNIT * 2])
        black_rect13 = self.canvas.create_rectangle(
            black_rect_center13[0] - 15, black_rect_center13[1] - 15,
            black_rect_center13[0] + 15, black_rect_center13[1] + 15,
            fill='black')
        self.black_rect.append(black_rect13)
        # black rect 14
        black_rect_center14 = refer + np.array([UNIT * 4, UNIT * 3])
        black_rect14 = self.canvas.create_rectangle(
            black_rect_center14[0] - 15, black_rect_center14[1] - 15,
            black_rect_center14[0] + 15, black_rect_center14[1] + 15,
            fill='black')
        self.black_rect.append(black_rect14)
        # black rect 15
        black_rect_center15 = refer + np.array([UNIT * 7, UNIT * 3])
        black_rect15 = self.canvas.create_rectangle(
            black_rect_center15[0] - 15, black_rect_center15[1] - 15,
            black_rect_center15[0] + 15, black_rect_center15[1] + 15,
            fill='black')
        self.black_rect.append(black_rect15)
        # black rect 16
        black_rect_center16 = refer + np.array([UNIT * 0, UNIT * 4])
        black_rect16 = self.canvas.create_rectangle(
            black_rect_center16[0] - 15, black_rect_center16[1] - 15,
            black_rect_center16[0] + 15, black_rect_center16[1] + 15,
            fill='black')
        self.black_rect.append(black_rect16)
        # black rect 17
        black_rect_center17 = refer + np.array([UNIT * 3, UNIT * 4])
        black_rect17 = self.canvas.create_rectangle(
            black_rect_center17[0] - 15, black_rect_center17[1] - 15,
            black_rect_center17[0] + 15, black_rect_center17[1] + 15,
            fill='black')
        self.black_rect.append(black_rect17)
        # black rect 18
        black_rect_center18 = refer + np.array([UNIT * 9, UNIT * 4])
        black_rect18 = self.canvas.create_rectangle(
            black_rect_center18[0] - 15, black_rect_center18[1] - 15,
            black_rect_center18[0] + 15, black_rect_center18[1] + 15,
            fill='black')
        self.black_rect.append(black_rect18)
        # black rect 19
        black_rect_center19 = refer + np.array([UNIT * 13, UNIT * 4])
        black_rect19 = self.canvas.create_rectangle(
            black_rect_center19[0] - 15, black_rect_center19[1] - 15,
            black_rect_center19[0] + 15, black_rect_center19[1] + 15,
            fill='black')
        self.black_rect.append(black_rect19)

        # create oval, yellow oval obstructions
        self.oval = []
        # oval1
        oval_center1 = refer + np.array([UNIT * 2, UNIT * 1])
        oval1 = self.canvas.create_oval(
            oval_center1[0] - 15, oval_center1[1] - 15,
            oval_center1[0] + 15, oval_center1[1] + 15,
            fill='yellow')
        self.oval.append(oval1)
        # oval2
        oval_center2 = refer + np.array([UNIT * 6, UNIT * 1])
        oval2 = self.canvas.create_oval(
            oval_center2[0] - 15, oval_center2[1] - 15,
            oval_center2[0] + 15, oval_center2[1] + 15,
            fill='yellow')
        self.oval.append(oval2)
        # oval3
        oval_center3 = refer + np.array([UNIT * 12, UNIT * 1])
        oval3 = self.canvas.create_oval(
            oval_center3[0] - 15, oval_center3[1] - 15,
            oval_center3[0] + 15, oval_center3[1] + 15,
            fill='yellow')
        self.oval.append(oval3)
        # oval4
        oval_center4 = refer + np.array([UNIT * 1, UNIT * 4])
        oval4 = self.canvas.create_oval(
            oval_center4[0] - 15, oval_center4[1] - 15,
            oval_center4[0] + 15, oval_center4[1] + 15,
            fill='yellow')
        self.oval.append(oval4)
        # oval5
        oval_center5 = refer + np.array([UNIT * 5, UNIT * 4])
        oval5 = self.canvas.create_oval(
            oval_center5[0] - 15, oval_center5[1] - 15,
            oval_center5[0] + 15, oval_center5[1] + 15,
            fill='yellow')
        self.oval.append(oval5)
        # oval6
        oval_center6 = refer + np.array([UNIT * 11, UNIT * 4])
        oval6 = self.canvas.create_oval(
            oval_center6[0] - 15, oval_center6[1] - 15,
            oval_center6[0] + 15, oval_center6[1] + 15,
            fill='yellow')
        self.oval.append(oval6)

        # create red rect(robots)
        self.rect = []
        rect1 = self.canvas.create_rectangle(
            origin1[0] - 15, origin1[1] - 15,
            origin1[0] + 15, origin1[1] + 15,
            fill='red')
        rect2 = self.canvas.create_rectangle(
            origin2[0] - 15, origin2[1] - 15,
            origin2[0] + 15, origin2[1] + 15,
            fill='red')
        self.rect.append(rect1)
        self.rect.append(rect2)

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect[0])
        self.canvas.delete(self.rect[1])
        # create origin
        refer = np.array([20, 20])
        origin1 = refer + np.array([UNIT * 0, UNIT * 1])
        origin2 = refer + np.array([UNIT * 0, UNIT * 3])
        # create red rect(robots)
        self.rect = []
        rect1 = self.canvas.create_rectangle(
            origin1[0] - 15, origin1[1] - 15,
            origin1[0] + 15, origin1[1] + 15,
            fill='red')
        rect2 = self.canvas.create_rectangle(
            origin2[0] - 15, origin2[1] - 15,
            origin2[0] + 15, origin2[1] + 15,
            fill='red')
        self.rect.append(rect1)
        self.rect.append(rect2)
        # return observation
        return [self.canvas.coords(self.rect[0]), self.canvas.coords(self.rect[1])]

    def step(self, action):
        s1 = self.canvas.coords(self.rect[0])
        s2 = self.canvas.coords(self.rect[1])
        base_action1 = np.array([0, 0])
        base_action2 = np.array([0, 0])
        base_action1[0] += UNIT
        base_action2[0] += UNIT
        if action == 0:   # 1up2up
            if s1[1] > UNIT:
                base_action1[1] -= UNIT
            if s2[1] > UNIT:
                base_action2[1] -= UNIT
        elif action == 1:   # 1up2down
            if s1[1] > UNIT:
                base_action1[1] -= UNIT
            if s2[1] < (MAZE_H - 1) * UNIT:
                base_action2[1] += UNIT
        elif action == 2:   # 1down2up
            if s1[1] < (MAZE_H - 1) * UNIT:
                base_action1[1] += UNIT
            if s2[1] > UNIT:
                base_action2[1] -= UNIT
        elif action == 3:   # 1down2down
            if s1[1] < (MAZE_H - 1) * UNIT:
                base_action1[1] += UNIT
            if s2[1] < (MAZE_H - 1) * UNIT:
                base_action2[1] += UNIT

        self.canvas.move(self.rect[0], base_action1[0], base_action1[1])  # move agent1
        self.canvas.move(self.rect[1], base_action2[0], base_action2[1])  # move agent2

        s1_ = self.canvas.coords(self.rect[0])  # next state
        s2_ = self.canvas.coords(self.rect[1])  # next state

        # reward function
        reward = 0
        # flag = 1 means nothing happened, reward = 8
        flag = 1
        # cal reward of black rect
        for i in range(len(self.black_rect)):
            if s1_ == self.canvas.coords(self.black_rect[i]):
                reward = reward - 10
                flag = 0
                done = False
            if s2_ == self.canvas.coords(self.black_rect[i]):
                reward = reward - 10
                flag = 0
                done = False
        for i in range(len(self.oval)):
            if s1_ == self.canvas.coords(self.oval[i]):
                reward = reward - 4
                flag = 0
                done = False
            if s2_ == self.canvas.coords(self.oval[i]):
                reward = reward - 4
                flag = 0
                done = False
        if s1_ == s2_:
            reward = reward - 10
            done = False
            flag = 0
        # avoid collision
        if flag == 1:
            reward = reward + 8
            done = False
            s2_ = 'terminal'
        # terminated
        if s1_[0] == (5 + 14 * UNIT):
            s1_ = 'terminal'
            done = True
        return [s1_, s2_], reward, done

    def render(self):
        time.sleep(0.5)
        self.update()


def update():
    for t in range(10):
        s1, s2 = env.reset()
        while True:
            env.render()
            a1 = 1
            a2 = 1
            s1, s2, r, done = env.step(a1, a2)
            if done:
                break

if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()