import gymnasium as gym
import numpy as np


def iterate_value_function(v_inp, gamma, env):
    ret = np.zeros(env.observation_space.n)
    for sid in range(env.observation_space.n):
        temp_v = np.zeros(env.action_space.n)
        for action in range(env.action_space.n):
            for (prob, dst_state, reward, is_final) in env.P[sid][action]:
                temp_v[action] += prob*(reward + gamma*v_inp[dst_state]*(not is_final))
        ret[sid] = max(temp_v)
    return ret


def build_greedy_policy(v_inp, gamma, env):
    new_policy = np.zeros(env.observation_space.n)
    for state_id in range(env.observation_space.n):
        profits = np.zeros(env.action_space.n)
        for action in range(env.action_space.n):
            for (prob, dst_state, reward, is_final) in env.P[state_id][action]:
                profits[action] += prob*(reward + gamma*v[dst_state])
        new_policy[state_id] = np.argmax(profits)
    return new_policy


env = gym.make("Taxi-v3")

gamma = 0.999999
cum_reward = 0
n_rounds = 500

for t_rounds in range(n_rounds):
    # init env and value function
    observation = env.reset()[0]
    v = np.zeros(env.observation_space.n)

    # solve MDP
    for _ in range(100):
        v_old = v.copy()
        v = iterate_value_function(v, gamma, env)
        if np.all(v == v_old):
            break
    policy = build_greedy_policy(v, gamma, env).astype(np.int64)

    # apply policy
    for t in range(1000):
        action = policy[observation]
        observation, reward, done, _, info = env.step(action)
        cum_reward += reward
        if done:
            break
    if t_rounds % 50 == 0 and t_rounds > 0:
        print(cum_reward * 1.0 / (t_rounds + 1))

env.close()