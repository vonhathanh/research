- When we define EC over finite field, it remains a group, but it becomes a cyclic group
- We can represent every number in a finite fields as an elliptic curve point and add them together just like we do in regular integer field
  - (5 + 7)mod p is homomorphic to 5G + 7G
- Generate EC y^2 = x^3 + 3 (mod 11). To solve the equation and determine which (x, y) points are on the curve, we'll need
  to compute sqrt(x^3 + 3)