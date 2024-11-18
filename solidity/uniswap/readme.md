## Overview
- An automated market maker (AMM)
- Hold two tokens (X, and Y) in a pool (a smart contract)
- Allow anyone to withdraw token X/Y from the pool, but they must deposit an amount of other token
such that the "total" asset stay constant
- Lets denote x = amount of token X in pool and y = amount of token Y in pool
- xy = x'y' (after the withdraw)
- Guarantee pool's asset can only stay the same or increase
- Most pools have fee
- Assets come from liquidity providers, who received a LP tokens to represent their share of the pool
- Advantages:
  - No bid-ask spread, price(x) = pool.balance(y) / pool.balance(x)
  - the actual price you pay will usually worse the than the "raw" price due to fee, slippage
  - Can be used as a free oracle (could be manipulated by flashloan)
  - No book-keeping orders so gas is more efficient
- Disavantages:
  - slippage could be high (just like spead in traditional MM)
  - MEV are usually unavoidable unless you use MEV RPC
  - LP must provide assets proportional to the current price -> no limit order (v3 fixed this issue)
  - LP might suffer from impermanent loss: missout gain if price of underlying asset increase, increases
  loss if underlying asset price decrease
- Uniswap follow core-periphery pattern:
  - Most essential logic is held in the core
  - Optional logic is in the periphery
  - Makes the core hold as little codes as possible (avoid bugs)
- Calculate the address of a pool by create2(factory, keccak256(token1, token2), salt)
  - No store access -> gas efficient
- Do not use EIP1167 clones because there is an extra 2600 gas per transaction due to delegate call

## Price impact
- Product of the two asset quantities in the pool (X times Y) at all times should remain constant at the very least
- x*y >= k
- In practice, we want to ensure that k_before <= k_after
- Assume we have a pool with: x= 100 usd, y = 100 eth
- We can't swap 25eth for 25usd since k_after = 125*75 = 9375 < k_before = 100*100 = 10000
- We can rearrange the equation to find delta usdc = 100 - k_before/125 = 20usdc
- You might give the AMM more than you should. For example, you could choose to take out only 18usdc instead of 20
- Fee only apply for the token deposited into the AMM, fee usually = 0.3%
- So the amount for swap is 99.7% = 25*0.97 = 24.925

## ERC4626 front run:
- Assume number of shares = sqrt(number of deposited token)
- At first, there is 10 shares and 100 underlying token (1 shares = 10 assets)
- If user deposit another 100 token they'll get sqrt(200) - 10 = 14 - 10 = 4 shares (1 shares = 14 assets)
- If another actor front run this tx and deposit 100 shares before the victim then the share victim would receive is
- sqrt(300) - 14 = 17 - 14 = 3 shares (lose 1 share)