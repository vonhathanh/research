- We can't apply value-based methods for env that have continuous space. For example, a robot arm that can move from 0-180 degree
- We can't run value function V() for every angle, this is impossible -> argmax operation is disabled
- Stochastic environments cause stability problems for value-based methods. Small perturbations in Q-values may lead to 
large changes in the policy of value-based methods
- Policy based method: start with a policy function then improve it by episodes with policy gradient method
- Policy-based methods find suitable continuous or stochastic policies directly without argmax()
- Stochastic policy perform exploration by nature, no need for epsilon greedy -> high variance, local optima, converge slower
- We also get rid of "perceptual aliasing": two states seem the same but need different acctions
- In value-based method: we take the maximum over Q-estimates, the action probabilities may change dramatically on a
small change (v_left 0.22, v_right = 0.21, -> always takes left, increase p_right to 0.23 -> always take right). 
- In policy-gradient method, the action preferences change smoothly over time
- How do we know if our policy is good?: we define a score function J(theta)
- J(theta) outputs the expected cumulated reward
![img_6.png](img_6.png)
- It's the weighted average by P(tau; theta) of all posisble values that the return R(tau) can take
![img_7.png](img_7.png)
- R(t): return from an arbitrary trajectory
- P(tau, theta): probability of each possible trajectory tau (depend on theta)
![img_8.png](img_8.png)
- We can’t calculate the true gradient of the objective function since it requires calculating the probability of 
each possible trajectory, which is computationally super expensive -> sample-based estimate -> local optimas
- To differentiate this objective function, we need to differentiate the state distribution, but we don't know it
- We need the Policy Gradient Theorem to differentiate it
![img_9.png](img_9.png)
- Gradient of log(policy(a, s)) is the direction of steepest increase of the log probability of selecting action at from st
- We multiply it with reward R(t), if R is positive -> push up the probability else push down
- We also collect multiple trajectories to average the gradient
- n-step Q learning: used in envs where rewards are sparse or delayed, helps the agent consider a broader context of future rewards
# Reinforce

- Start with a parameterized policy function pi_theta
- Sample a trajectory tau
- If it's good, increase the parameters towards tau, otherwise decrease them
- Keep doing this until converge
- To know which policy is best, we need some kind of measure of its quality -> a value J
- It is natural to use the value function of the start state as our measure of quality J(theta) = V(s0)
- We wish to maximize J, if our policy is differentiable, then we can use gradient ascent: 
![img_3.png](img_3.png)
- Our final goal is to update the parameters theta so that we find the optimal policy
- If action a is better, we want to increase the parameter theta but we don't know which action is the best
- So we take a sample trajectory and estimates the value of the actions
- We use Q(s, a) to do that, Q() can be any function: discounted return, advantage function...
![img_2.png](img_2.png)
- A problem with this formula is that better action got pushed more frequently, create high bias in our model
- We can correct by dividing by the general probability

# Actor Critic Bootstrapping

- REINFORCE is low bias, high variance since the full episode is sampled
- Actor critic combine the value-based with policy-based approach
- Variance comes from two sources: cumulative reward estimate and gradient estimate
-> bootstrapping for better reward estimates, and baseline subtraction to lower the variance of gradient estimates
- Both methods use a learned value function V(s)