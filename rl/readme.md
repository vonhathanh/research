# Value-based method

- When we in a state S, we use value function V(s) to estimate how much reward we could get if we follow the current policy R
- At initialization, we have no knowledge of V(s) so V(s) = 0 for all s
- As the agent learn, we gradually update our knowledge of V(s) using V(s'), reward and V(s)
- We want V(s) goes closer to V^*(s). The idea is V(s) is also closer to V(s') because it's the next state
- V(s) = alpha*reward + discounted future reward + V(s') - V(s)