## Information

- Information I of an event x observed from distribution p(X) is defined as: I(x) = -log(p(x))
- p(x) in [0, 1], => log(p(x)) in [infinity, 0]
- The more likely an observation is (higher p(x)) the less information we get when we actually observe the event
- For example, if we buy a lottery with 6 numbers, p(x=win) is 1/10**6 which is extremely small. When this event occur, 
it brings lots of information. In contrast, if we happen to buy lose lottery (which is the genera case p(x) ~= 1), 
those lottery numbers bring tiny amount of information as we already expect we won't be able to win the lottery anyway

## Entropy

- Measures uncertainty in a distribution p(X) or the "spread"
- We usually denote H as the entropy
- H(P) = -sum(p(x)log(p(x))) where x in X: sum of all information I(x) multiplied by the probability of event x
- H(P) reaches max when there is an evenly distribution between the events

## Cross Entropy

- In optimization problems, we usually have two distribution, target Q(x) and estimate P(x)
- We want to measure the "inefficient" when we use P(x) to encode data from Q(x)
- If H(P, Q) == H(Q) then we optimized the distribution sucessfully
- H(P, Q) = -sum(p(x)log(q(x))) where x in set X

## KL-divergent

- Similar to cross-entropy, KL-divergent measure the different between P(x) and Q(x) 
- KL-divergent always >= 0
- KL(P, Q) = H(P, Q) - H(P)