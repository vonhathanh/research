- Bilinear pairing: allows us to take three numbers: a, b, and c where ab = c, encrypt them to become E(a), E(b), E(c)
  where E is an encryption function, send the two encrypted values to a verifier who can verify E(a)E(b) = E(c) but not now
  the original values
- How numbers are encrypted: multiply a scalar by a point on an EC, we get another point: P = pG where p is a scala and
  G is the generator. Given P and G, we can't determine p
- Assume pq = r, we take P = pG, Q = qG, and R = rG and convince a verifer that the "preimages" of P and Q multiply to produce 
  the preimage of R, we want a function such that: f(P, Q) = R and not equal to R when p*q != r
- Our bilinear pairing is a special function that if we plug in EC points into the argument of f(P1, P2) we can
  determine p*q = r without knowing p, q, and r
- Feature of bilinear: f(aG, bG) = f(abG, G) = f(G, abG)
- In the literature, we write: e: GxG->G_t (target group)
- In practice, it turns out to be easier to create bilinear pairings when different groups are used.
  e(a, b) -> c: a in G1, b in G2, c in G3
- The property we care still hold: e(aG1, bG2) = e(abG1, G2) = e(G1, abG2)
- G3 is the codomain of e(G1, G2)
- There are two type of pairings: symetric (the generator and EC group are the same in both argument of E)
  asymetric:the generator and EC group are different group
- Ethereum chooses to use EC with field extensions (FE). Each point in EC extension consists of several (x, y) pairs
- The chances that e(aG, bG′) = e(abG, G′) = e(G,abG′) is true for three random groups is very slim so we use FE