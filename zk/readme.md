- Congruent: two numbers are called congruent if they share the same remainder when dividing by p
  - Example: if p = 7, then 12 is congruent to 5 because 5mod7 = 12mod7 = 5

- Order of the field: number of elements in the field

- Additive Inverse (AI): the additive inverse of a is a number b such that a + b = 0
  - Zero is its own additive inverse
  - Every number has exactly one additive inverse

- Multiplicative inverse(MI): the MI of a is a number b such that a*b = 1
  - Zero has no MI
  - 1 is its own MI
  - Every number (except 0) has exactly one MI (which could be itself)
  - The element of value (p-1) is its own MI (because p-1 is congruent to -1 and -1 is it own MI)

- Computing the multiplicative inverse with Fermat’s Little Theorem: a^(p-2) = a^-1

- The addition of multiplicative inverses is consistent with “regular” addition of fractions
  - With p = 7, 4 and 2 are MI of each other -> 4 is congruent to 1/2 and 2 is congruent to 1/4, if we add 1/2 + 1/2.
We get 1 <=> 4 + 4 = 8 (mod 7) = 1

- The general way to compute a “fraction” in a finite field is the numerator times the multiplicative inverse of the denominator, modulo p
```python
def compute_field_element_from_fraction(num, den, p):
    inv_den = pow(den, -1, p)
    return (num * inv_den) % p
```
It is not possible to do this when the denominator is a multiple of p. For example, 1/7 cannot be represented in the finite field p = 7.
Because pow(7, -1, 7) has no solution (7 is not an element in the field too)

- Finite field division does not suffer from precision loss: we can represent 1/3 in finite field, it's just MI of 3

- Finite field elements do not have a tradition of odd or even. 
In a finite field, any element can be divided by two with no remainder. 
This is because dividing by two is just multiply with MI of 2 and that always result another field element without remainder

- No two elements can be multiplied together to obtain zero in a finite field unless one of them is zero itself

- Finite field operations are associative, commutative and distributive
  - associative: (a + b) + c = a + (b + c) (mod p)
  - commutative: (a + b) = (b + a) (mod p), ab = ba(mod p)
  - distributive: a(b + c) = ab + ac (mod p)

- Elements in a finite field does not have to be perfect squares to have a square root
  - Example: p = 11, 5x5 (mod p) = 3 -> 5 is the square root of 3
  - Just like regular square roots, modular square roots in a finite field also have 2 solution (except 0 has only 1)
  - The second square root is always the additive inverse of the first square root

- Linear systems of equations in finite fields
  - Finite field systems of equations have:
    - No solution
    - One solution
    - p solution
  - A linear system of equations over real numbers has zero, one, or infinite solutions does not imply that
  the same linear system of equations over a finite field will also have the same number of solutions

- Polynomials in finite fields: polynomials in finite fields share a lot of properties with polynomials over real numbers:
  - A polynomial of degree d has at most d roots
  - Adding polynomials in a finite field follows associative, commutative, and distributive laws
  - If we multiply two polynomials p1 and p2, the roots of the product will be the union of the roots of p1 and p2
  - Polynomials that do not have roots in real numbers may have roots in finite field, for example: y = x^2 + 1 with p = 17
In finite field, we just need to find x^2 = 16 since 16+1 = 17 (mod 17) = 0
  - The reverse also apply, polynomials with real roots may have no roots in a finite field
- Limitations in arithmetic circuits for ZK proofs: If we wish to write an arithmetic circuit to show "I know the root of the polynomial: y = x^2 - 5"
in finite field. Then we may run into the issue of not being able to represent 5^-1
  