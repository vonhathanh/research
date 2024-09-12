- Encrypted Exponentiation: with bilinear pairing, we can do (partially) homomorphic encryption for multiplication. But we can't do it with exponents
- The output of our previous pairing was an EC point in G12 which have 12 dimensions. If we construct a pairing with that point again, the output would be a group with massive dimension.
- Let's say we want to prove we know x such that: x^3 - 4x^2 + 3x - 1 = 0
- We can't give x to the verifier, so we encrypt it with G1, x' = xG1. The problem is the verifier can't compute
x^3 due to pairing can't be used twice, so our solution is to calculate all encrypted x, x^2, x^3 and give it to the verifier
- Trusted setup: typically, we use the above construction in reverse. Mainly because this algorithm requires the verifier
to do work linearly proportional to the size of the polynomial. We want succinct proof not a linear one
- 
