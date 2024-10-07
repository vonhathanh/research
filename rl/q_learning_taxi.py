import random

import gymnasium as gym
import numpy as np

env = gym.make("Taxi-v3")

Q = np.zeros((env.observation_space.n, env.action_space.n))

gamma = 0.7 # discount factor
alpha = 0.2 # learning rate
epsilon = 0.1 # exploration rate

for episode in range(10000):
    done = False
    total_reward = 0
    state, info = env.reset()

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample(info["action_mask"])
        else:
            action = np.argmax(Q[state])

        next_state, reward, done, _, info = env.step(action)

        next_max = np.max(Q[next_state])
        old_v = Q[state, action]

        new_v = old_v + alpha * (reward + gamma * next_max - old_v)

        Q[state, action] = new_v
        total_reward += reward
        state = next_state

    if episode % 100 == 0:
        print(f"Episode: {episode}, total reward: {total_reward}")