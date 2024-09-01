A ring is set with two binary operators such that:
  - Under the first binary operator, the set is an abelian group
  - Under the second binary operator, the set is a monoid. We do not require the monoid to be commutative. If it is, we refer
to this as an abelian ring
  - The second binary operator distributes over the first: let say @ is the first and * is the second binary operator
    - (a @ b) * c = (a * c) @ (b * c)
    - c * (a @ b) = (c * a) @ (c * b)
    - We do not require c @ (a * b) to be distributed
    - Note that (a @ b) * c = c * (a @ b) does not necessarily true
    - Proof: as in the definition, under the second binary operator, the set is a monoid. This means the operator * is not
commutative, which leads to a*c != c*a. Note: chatgpt agrees with our solution while claudeAI is not, but we'll take the tutorial fact rather than believe in LLM
- Example: trivial ring, a ring with only {0} under addition and multiplication is a trivial ring
    Proof:
      - Additive structure (abelian group):
        - Closure: 0 + 0 = 0
        - Associativity: (0 + 0) + 0 = 0 + (0 + 0) = 0
        - Identity: 0 is the additive identity since 0 + 0 = 0
        - Inverse: 0 is its own additive inverse since 0 + 0 = 0
      - Commutativity: 0 + 0 = 0 + 0
        - Multiplicative structure (monoid):
        - Closure: 0 * 0 = 0
      - Associativity: (0 * 0) * 0 = 0 * (0 * 0) = 0
        - Note: There is no multiplicative identity in this ring, but that's okay. A ring doesn't require a multiplicative identity (rings that do have one are called rings with unity or unital rings).
      - Distributive property:
        - Left distributivity: 0 * (0 + 0) = 0 = (0 * 0) + (0 * 0)
        - Right distributivity: (0 + 0) * 0 = 0 = (0 * 0) + (0 * 0)
- Square matrices of real numbers under addition and multiplication is a ring
- Proof: let call the three basic elements of our ring a, b, and c 
  - Additive structure (abelian group):
    - Closure: a + b = c (still a square matrix)
    - Associativity: (a + b) + c = a + (b + c)
    - Identity: zero matrix (maxtrix will all element is zero) is the additive identity since a + 0 = a
    - Inverse: multiply any matrix with -1, and we get it's inverse
  - multiplicative structure:
    - Closure: a*b = d (still a square matrix)
    - Identity element: identity matrix where the diagonal elements are 1
    - Assiciativity: (a * b) * c = a * (b * c), this only hold in square matrix
  - Distributive property:
  - Left distributivity: a * (b + c) = d = (a * b) + (a * c)
  - Right distributivity: similar to left distributivty
- Should a ring always have an inverse? We assume it has, but not every one does that
- Field: a set that has two binary operators:
  - Under the first operator, it's an abelian group
  - Under the second operator, excluding the zero element, it's an abelian group
  - A field allow us to exclude the "problematic element" out of the set
- There is no trivial field: Usually we need two identity elements to forms a field. One for the first operator and the
other one is for the second operator. If we construct a field with only one indentity element for both operators. If we choose 1
to be the identity then it's not valid because a + 1 != a. If we choose 0 then it's not valid because the zero element is removed.
An empty set can't be a group (a trivial group must have atleast one element)
- Field extensions: A set can have a subset. Because field is a set, we can also have subfields. For example, rational
numbers are subfield of real numbers. Therefore, we can say that real numbers are a field extension of rational numbers 
- You can't just pick any subset, for a subset to becomes subfield, it's operator must be closed,
- Finite fields (FF): one major advantage of FF is that we can do arithmetic on rational numbers of abitrary precision. Like 1/3
- This doesn't mean we can recover the original ration numbers given an element in the FF. The mapping from rational numbers
to FF is surjective.
- If we are trying to convince a verifier that we did some math on rational numbers correctly, the verifier only need to 
check the claim in FF.
- FF behaves like regular fields: any addition, subtraction, multiplication and division we do with integers is also true
in a prime finite field
- If you do the operations like: square root, taking the derivative then you lose the guarantee, those are not binary
operators for a field