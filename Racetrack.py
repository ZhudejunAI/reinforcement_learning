# coding=utf8
import random
import numpy as np

# 先纵向移动,再横向移动,确保赛车是向右穿过终点

map1 = [[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

start_location = [[31, 3], [31, 4], [31, 5], [31, 6], [31, 7], [31, 8]]


class Track(object):
    def __init__(self, map_track):
        self.map = map_track
        i = random.randint(0, 5)
        self.x, self.y = start_location[i]
        self.vx = 0
        self.vy = 0

    def judgement_bound(self, action):
        x, y = action
        temp_x = self.x + x
        temp_y = self.y + y
        if 0 <= temp_x < 6 and temp_y > 16:
            return 3
        elif temp_x < 0 or temp_x > 31 or temp_y < 0 or temp_y > 16:
            return -1
        elif self.map[temp_x][temp_y] == 0:
            return -1
        else:
            return 1

    def at_starting_line(self):
        if self.x == 31 and 3 <= self.y < 9:
            return True
        else:
            return False

    def back_to_start(self):
        loc = random.randint(0, 5)
        self.x, self.y = start_location[loc]
        self.vx = 0
        self.vy = 0

    def get_an_action(self):
        while True:
            epsilon = random.randint(1, 10)
            if epsilon == 5:
                action_x = action_y = 0
                temp_vx = self.vx
                temp_vy = self.vy
            else:
                while True:
                    id1 = random.randint(1, 3)
                    action_x = id1 - 2
                    temp_vx = self.vx + action_x
                    if -5 < temp_vx < 5:
                        break

                while True:
                    id2 = random.randint(1, 3)
                    action_y = id2 - 2
                    temp_vy = self.vy + action_y
                    if -5 < temp_vy < 5:
                        break

            if temp_vx == 0 and temp_vy == 0 and self.at_starting_line() == False:
                continue
            else:
                break

        return action_x, action_y

    def step(self):
        action_x, action_y = self.get_an_action()
        try_action = (self.vx + action_x, self.vy + action_y)
        step_state = self.judgement_bound(try_action)
        if step_state == 3:
            return 0, action_x, action_y, step_state
        elif step_state == 1:
            return -1, action_x, action_y, step_state
        else:
            return -1, action_x, action_y, step_state


class MonteCarlo(object):
    def __init__(self, map_mc):
        self.q = np.zeros((32, 17, 9))
        self.c = np.zeros((32, 17, 9))
        self.pi = np.zeros((32, 17))
        self.track = Track(map_mc)
        self.index_action = [[1, 1], [1, 0], [1, -1], [0, 1], [0, 0], [0, -1], [-1, 1], [-1, 0], [-1, -1]]

    def off_policy_mc(self, iters):
        i = 0
        while i < iters:
            history = []
            self.track.back_to_start()
            while True:
                reward, ax, ay, step_state = self.track.step()
                comb_action = [ax, ay]
                seq_action = self.index_action.index(comb_action)
                result = (self.track.x, self.track.y, seq_action, reward)
                history.append(result)
                if reward == 0:
                    break
                if step_state == 1:
                    self.track.vx += ax
                    self.track.vy += ay
                    self.track.x += self.track.vx
                    self.track.y += self.track.vy
                elif step_state == -1:
                    self.track.back_to_start()

            G = 0.0
            W = 1.0
            gamma = 0.9
            t = len(history) - 2
            print('t=%d' % t)
            while t >= -1:
                loc_x, loc_y, seq_action, r = history[t + 1]
                G = gamma * G + r
                self.c[loc_x, loc_y, seq_action] += W
                self.q[loc_x, loc_y, seq_action] += (W / self.c[loc_x, loc_y, seq_action]) * (
                G - self.q[loc_x, loc_y, seq_action])
                self.pi[loc_x, loc_y] = np.argmax(self.q[loc_x, loc_y, :])
                if seq_action != self.pi[loc_x, loc_y]:
                    break
                W *= 9
                t -= 1
                print i, G, r, W
            i += 1


if __name__ == '__main__':
    mc = MonteCarlo(map1)
    mc.off_policy_mc(10000)
    print mc.q
    print('*****************************************')
    print mc.pi
