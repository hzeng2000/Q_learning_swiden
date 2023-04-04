"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from black_white_env import Maze
from RL_brain import QLearningTable

total_episode = 100
def update():
    for episode in range(total_episode):
        # initial observation
        observation = env.reset()
        episode_reward = 0
        ebs_list = []
        ebs_list.append(observation)
        # fresh env
        env.render()

        while True:
            # RL choose action based on observation
            # 0:up 1:down, [0] is robot1 and [1] is robot2
            action = RL.choose_action(str(observation), episode)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_
            # fresh env
            env.render()

            # break while loop when end of this episode
            if done:
                break

            # reward sum
            episode_reward = episode_reward + reward
            ebs_list.append(observation)

        print("episode : {} total reward: {}".format(episode, episode_reward))

    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)), total_episode=100)

    env.after(100, update)
    env.mainloop()