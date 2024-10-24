from collections import deque, namedtuple

import gymnasium as gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

import numpy as np

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class ActorCritic(nn.Module):
    def __init__(self, s_size, a_size, h_size):
        super(ActorCritic, self).__init__()
        # Create two fully connected layers
        self.feature_layer = nn.Sequential(nn.Linear(s_size, h_size), nn.ReLU())
        # Actor head (policy network)
        self.actor = nn.Sequential(
            nn.Linear(h_size, h_size),
            nn.ReLU(),
            nn.Linear(h_size, a_size)
        )
        # Critic head (value network)
        self.critic = nn.Sequential(
            nn.Linear(h_size, h_size),
            nn.ReLU(),
            nn.Linear(h_size, 1)
        )

    def forward(self, x):
        features = self.feature_layer(x)
        # Actor: probability distribution over actions
        action_probs = F.softmax(self.actor(features), dim=-1)
        # Critic: state value estimate
        state_value = self.critic(features)
        return action_probs, state_value

    def act(self, state):
        """
        Given a state, take action
        """
        state = torch.from_numpy(state).float().to(device)
        probs, _ = self.forward(state)
        m = Categorical(probs)
        action = m.sample()
        return action.item(), m.log_prob(action)


env = gym.make("CartPole-v1")

# Get the state space and action space
s_size = env.observation_space.shape[0]
a_size = env.action_space.n

Transition = namedtuple('Transition',
                        ('state', 'action', 'reward', 'next_state', 'done'))

def update(policy: ActorCritic, transitions: list[Transition], gamma: float, optimizer):
    states = torch.FloatTensor([t.state for t in transitions]).to(device)
    actions = torch.LongTensor([t.action for t in transitions]).to(device)
    rewards = torch.FloatTensor([t.reward for t in transitions]).to(device)
    next_states = torch.FloatTensor([t.next_state for t in transitions]).to(device)
    dones = torch.FloatTensor([t.done for t in transitions]).to(device)

    # Calculate returns and advantages
    action_probs, state_values = policy(states)
    _, next_state_values = policy(next_states)

    returns = []
    R = next_state_values[-1] * (1 - dones[-1])
    for r in reversed(rewards):
        R = r + gamma * R
        returns.insert(0, R)

    returns = torch.stack(returns)

    # Calculate advantages
    advantages = returns - state_values.squeeze()

    # Get action probabilities and calculate log probs
    dist = Categorical(action_probs)
    log_probs = dist.log_prob(actions)

    # Calculate losses
    actor_loss = -(log_probs * advantages).mean()
    critic_loss = F.mse_loss(state_values.squeeze(), returns.squeeze())

    # Add entropy term for exploration
    entropy_loss = -0.01 * dist.entropy().mean()

    # Total loss
    total_loss = actor_loss + 0.5 * critic_loss + entropy_loss

    # Update network
    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()

    return total_loss.item()

def a2c(policy: ActorCritic, optimizer, n_training_episodes, max_t, gamma, policy_weight, print_every):
    scores = []
    for i_episode in range(1, n_training_episodes + 1):
        # print("current episode ", i_episode)
        state, _ = env.reset()
        score = 0.0
        transitions = []

        for t in range(max_t):
            action, log_prob = policy.act(state)

            next_state, reward, done, _, _ = env.step(action)

            score += reward

            transitions.append(Transition(state, action, reward, next_state, done))

            state = next_state

            if done:
                break

        loss = update(policy, transitions, gamma, optimizer)

        scores.append(score)

        if i_episode % print_every == 0:
            print("loss: ", loss)
            print('Episode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores)))

    return scores


cartpole_hyperparameters = {
    "h_size": 128,
    "n_training_episodes": 1000,
    "n_evaluation_episodes": 10,
    "max_t": 500,
    "gamma": 0.99,
    "lr": 1e-3,
    "env_id": "CartPole-v1",
    "state_space": s_size,
    "action_space": a_size,
    "policy_weight": 0.5,
}

# Create policy and place it to the device
cartpole_policy = ActorCritic(cartpole_hyperparameters["state_space"], cartpole_hyperparameters["action_space"],
                         cartpole_hyperparameters["h_size"]).to(device)
cartpole_optimizer = optim.Adam(cartpole_policy.parameters(), lr=cartpole_hyperparameters["lr"])

scores = a2c(cartpole_policy,
             cartpole_optimizer,
             cartpole_hyperparameters["n_training_episodes"],
             cartpole_hyperparameters["max_t"],
             cartpole_hyperparameters["gamma"],
             cartpole_hyperparameters["policy_weight"],
             10)
