import gymnasium as gym
import numpy as np

def monte_carlo(n_samples, ep_length, alpha, gamma):
    # 0: initialize
    t = 0; total_t = 0
    Qsa = []

    # sample n_times
    while total_t < n_samples:

        # 1: generate a full episode
        s = env.reset()
        s_ep = []
        a_ep = []
        r_ep = []
        for t in range(ep_length):
            a = select_action(s, Qsa)
            s_next, r, done = env.step(a)
            s_ep.append(s)
            a_ep.append(a)
            r_ep.append(r)

            total_t += 1
            if done or total_t >= n_samples:
                break
            s = s_next

        # 2: update Q function with a full episode (incremental implementation)
        g = 0.0
        for t in reversed(range(len(a_ep))):
            s = s_ep[t]; a = a_ep[t]
            g = r_ep[t] + gamma * g
            Qsa[s,a] = Qsa[s,a] + alpha * (g - Qsa[s,a])

    return Qsa

def select_action(s, Qsa):
    # policy is egreedy
    epsilon = 0.1
    if np.random.rand() < epsilon:
        a = np.random.randint(low=0, high=env.n_actions)
    else:
        a = np.argmax(Qsa[s])
    return a

env = gym.make('Taxi-v3')
monte_carlo(n_samples=10000, ep_length=100, alpha=0.1, gamma=0.99)