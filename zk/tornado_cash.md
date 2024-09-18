- ZK proofs do not carry out the computation, they prove the validity of a computation, not knowledge of a certian fact
- They take an agreed-upon computation, a proof the computation was carried out, and the result of the computation, 
  then determine if the prover really ran the computation and produced the output. 
- The zero knowledge part comes from the optional feature that the proof-of-computation can be represented in a way that
  gives no information about the inputs
- To generate, but not verify, a zero knowledge proof of a computation, you must actually carry out the computation.
- Example of Tornado Cash: I know two secret numbers and the proof is the
- Core strategy of Tornado Cash: mixing the depositors and withdrawers
  - Deposit/withdraw the same amount tokens
- Tornado Cash without zk: depositor picks two random numbers, concat them and then hash the result -> send to TC to store the hash
- Tornado Cash with zk: withdrawer can demonstrate they know the preimage of one of the hashes without revealing
  which hash it is and without revealing the preimage of the hash
- All deposit hashes are publicly known -> We need a data structure that can compactly hold a lot of hashes -> Merkle Tree
- Rather than looping all the hashes, we can say: I know the preimage of one of the hashes and the hashes is in the merkle tree
- User need to produce a leaf hash preimage, then prove that leaf hash is in the merkle tree via merkle proof
- Zero knowledge proofs let us prove that we generated a valid Merkle proof against the public Merkle root as well as the 
preimage of the leaf – without showing how we conducted that computation.
- To prevent user withdraw multiple times, TC use nullifier scheme
- The two numbers that go into the deposit hash were nullifier nonce and a random number
- User must: submit the hash of nullifier, and proof they concatenated (nullifier, random number)
- Incremental Merkle Tree: Tree of fixed depth (32)
  - All subtrees to the right of the newest member consists of merkle subtrees with all zero leafs
  - We cache those subtrees -> need a cache to store 32 root of subtrees of level 1->32
  - We can also cache all subtree on the left of the newest nodes -> maximum 32 subtrees
  - We only need 32 iterations to compute the whole merkle tree
- Merkle roots always change when users make new deposit, TC store the last 30 roots, so user don't have to work
  with the newest root every time they want to withdraw