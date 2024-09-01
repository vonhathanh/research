- Sometimes binary operators are other binary operators in disguise. 
For example, when dealing with groups that only have addition, sometimes writers casually refer to multiplication 
even though the group does not have that binary operator. 
What multiplication is in this context is really shorthand for repeating an addition operation a certain number of times
- Excersize 1: Integers (positive and negatives) are not a group under multiplication. The reason is that most elements in
the set lack of inverse element. For example, if the identity element is 1, then inverse of element a is a' must satisfy
this: a*a' = 1, which lead to a' = 1/a, this creates rational number, not integer number. The only number that satisfy
this property is 1, because 1*1 = 1;
- A group doesn't require the inverse to be computable by group laws. For example, with matrix addition, the binary operator
is addition, but we can multiply a MxN maxtrix with -1 to get the inverse matrix
- Finite group: has finite number of elements in it and can be expressed by a Cayley table
- ![img_5.png](img_5.png)
- In Cayley table: each row contains no duplicate and each column contains no duplicate
- Cyclic group is a group that has an element that can generate all elements of the group by applying the binary
operator repeatedly to that element, or to it's inverse.
- Generator is usually denoted with g or G
- If a group is cyclic, then it's abelian. Note that the converse of this statement is not always true
- The identity element of a group is unique. Proof: let's assume the contracdiction is true, so a group A has two
identity elements E and I. The property of identity element allow us to have: a + a' = E and a + a' = I where a
is an elemement of A and a' is it inverse. If this is true then E and I are diffefrent number, which means a + a' != a + a'
which is wrong.
- Group homomorphisms: let A be a group with binary operator $ and B be a group with binary operator #. Group A is
homomorphic to group B if there exists a transformation d where d maps elements from A to B and for all a, a'
d(a $ a') = d(a) # d(a').
- Example: let A be group of integers under addition and B be group of power of 2 under multiplication
the transformation is d(2^x), 2^(a + b) = 2^a*2^b
- We sometimes call d a structure preserving transformation. If the transformation is hard to invert then we have
homomorphic encryption