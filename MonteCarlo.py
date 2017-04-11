#coding=utf-8
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

ACTION = ['hit','stick']
TERMINAL = (-1,-1)


class Blackjack(object):
    def __init__(self):
        self.card_num = 0
        self.sum = 0
        self.has_ace = False

    def bust(self):
        if self.sum > 21:
            return True
        else:
            return False

    def natural(self):
        if self.card_num == 2 and self.has_ace and self.sum == 11:
            return True
        else:
            return False

    def count_sum(self):
        if self.has_ace:
            return self.sum
        else:
            if self.sum + 10 > 21:
                return self.sum
            else:
                return self.sum + 10

    def get_one_card(self):
        number = random.randint(1, 13)
        if number > 10:
            number = 10
        if number == 1:
            self.has_ace = True
        self.card_num += 1
        self.sum += number

    def start_game(self):
        first = random.randint(1, 13)
        if first > 10:
            first = 10
        second = random.randint(1, 13)
        if second > 10:
            second = 10

        if first == 1 or second == 1:
            self.has_ace = True
        else:
            self.has_ace = False

        self.card_num = 2
        self.sum = first + second


class MC(object):
    def __init__(self):
        self.q = np.zeros((21, 21, 2))
        self.value = np.zeros((21, 21))
        self.c = np.zeros((21, 21, 2))
        self.dealer = Blackjack()
        self.player = Blackjack()

    def step(self, action):
        if action == ACTION[0]:
            self.player.get_one_card()
            if self.player.bust():
                return TERMINAL, -1
            else:
                return (self.dealer.sum, self.player.sum), 0
        else:
            while(self.dealer.sum < 17):
                self.dealer.get_one_card()
                if self.dealer.bust():
                    return TERMINAL, 1
            one = self.dealer.count_sum()
            two = self.player.count_sum()
            if one > two:
                return TERMINAL, -1
            elif one == two:
                return TERMINAL, 0
            else:
                return TERMINAL, 1

    def new_game(self):
        self.dealer.start_game()
        self.player.start_game()
        if self.player.natural():
            if self.dealer.natural():
                return TERMINAL, 0
            else:
                return TERMINAL, 1
        else:
            return (self.dealer.sum, self.player.sum), 0

    def run(self, iters):
        for _ in xrange(iters):
            history = []
            state, reward = self.new_game()
            while not state == TERMINAL:
                action = 0
                if state[1] == 20 or state[1] == 21:
                    action = 1
                next_state, reward = self.step(ACTION[action])
                history.append((state, action, reward))
                state = next_state

            G = 0
            for i in range(len(history)-1, -1, -1):
                state, action, reward = history[i]
                G += reward
                self.c[state[0]-1, state[1]-1, action] += 1
                self.q[state[0]-1, state[1]-1, action] += (G - self.q[state[0]-1, state[1]-1, action])

    def optimal(self):
        for i in range(21):
            for j in range(21):
                self.value[i,j] = self.q[i,j,np.argmax(self.q[i,j,:])]


if __name__ == '__main__':
    mc = MC()
    mc.run(1000000)
    mc.optimal()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(0, 21, 1)
    Y = np.arange(0, 21, 1)
    X, Y = np.meshgrid(X, Y)

    Z = mc.value[X, Y]
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()

    for i in range(0,21):
        for j in range(0,21):
            print mc.value[i,j],
        print