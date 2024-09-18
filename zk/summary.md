- We start with R1CS: Ls*Rs = Os
  - L, R, O are nxm matrices. n = number of constraints (each constraint is a quadratic multiplication), m = length of the witness vector (s.length)
- We use the φ transformation operator to convert R1CS to QAP (columns to polynomials)
  - U(x) = φ(L), V(x) = φ(R), W(x) = φ(R), a = φ(s). They become a vector of m polynomials
  - U(x) = u_0(x), u_1(x),...,u_m(x) where each u_i(x) is a vector that contains the coefficients of the homomorphic polynomial
  - Each polynomial has the same degree n-1, since we need n-1 degree polynomial to travel through n points 
  {x, y where x = {1,...n, y = L[i, 0] for i from 0→n-1}
  - After transforming L, R, O, s to QAP, our problem becomes: (U*a)(V*a) = W*a  (* is dot product)
  - U*a is a polynomial because we take the dot product of two vectors of polynomial: 
  - U*a = {u_1(x), u_2(x)...u_m(x)} * {a_1, a_2,..., a_m} = a_1*u_1(x) + a_2*u_2(x)+...+a_m*u_m(x)
  - (U*a)(V*a) = W*a is not balanced because degree of (U*a)(V*a) = z will usually > degree of (W*a)
  - We need to add a balancing term, which is also a polynomial that is evaluated to y = 0 at x = {1, 2, ..., z}
  - We can derive that polynomial easily using the formula: p(x) = (x-1)(x-2)...(x-z) but the real form is: h(x)t(x)
  - Why do we use h(x)t(x) instead of a fixed formula? it's because t(x) will have the form of (x-1)(x-2)(x-3)...(x-n)
  and h(x) = ((U*a)(V*a) - W*a)/t(x). The QAP convert R1CS to vector of polynomials, these polynomials pass through
  - x = {1, 2, 3, ..n) so they will divide by t(x)
  - When we multiply 2 polynomials, the root will be the union of the two, so the result will also divide by t(x)
  - If the prover give a valid proof, then it will divide by t(x)
  - Of course, this alone will not enough to enforce prover to honest
- Back to Schwartz-Zippel
  - We can check if two polynomials are equal: (U*a)(V*a) = W*a + h(x)t(x) using a single random point
  - That random point must be encrypted otherwise prover could cheat the verifier
  - We need a trusted setup (third-party) to do that for us, it would compute the exponent of random point x
  in the exponent of G1: [xG], [x^2G], ...[x^nG]
  - So the evaluation becomes: (U*a)(x) * (V*a)(x) = W*a(x) + h(x)t(x)
  - Remember U*a is just a polynomial so we can expand the term to: A = (U*a)(x) = u_d(x^d) + u_(d-1)((x^(d-1)))... + u_0
  = u_d(x^dG) + u_(d-1)((x^(d-1)G))... + u_0G
- Now it's the hard part, using QAP alone can't prevent prover from forge fake values, so we need groth16 to help us