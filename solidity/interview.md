1. What is the difference between private, internal, public, and external functions?
private: not visible child contracts, EOAs can't call them
internal: similar to private but visible to child contracts
public: visible to all child contracts, EOAs can interact with the contract using these functions
external: similar to public but contract itself can't use them (use less gas than public fn because public fn copy data to memory, external fn use data from calldata directly)
2. Approximately, how large can a smart contract be? 24kb
3. What is the difference between create and create2?
- create: address = keccak256(rlp([sender_address,sender_nonce]))[12:]
- create2: 
    initialisation_code = memory[offset:offset+size]
    address = keccak256(0xff + sender_address + salt + keccak256(initialisation_code))[12:]
    salt allows the new contract to be deployed at a consistent, deterministic address.
4. What major change with arithmetic happened with Solidity 0.8.0? safemath included, overflow revert
5. What special CALL is required for proxies to work? delegatecall
6. How do you calculate the dollar cost of an Ethereum transaction?
- Before EIP-1559: (gas used * gas price / 10**9) * ether price, (gas used * gas price / 10**9) = total ether cost
- After EIP-1559: (((BASE_FEE + PRIORITY_FEE) * GAS_USED)/10**9)*ether price, miner receives priority fee, base fee is burned
7. What are the challenges of creating a random number on the blockchain? everything is deterministic
8. What is the difference between a Dutch Auction and an English Auction?
- Dutch auction: price is decayed over time
- English auction: price is increased over time
9. What is the difference between transfer and transferFrom in ERC20?
- transfer: use your own money
- transferFrom: use allowance from somebody to transfer money
10. Which is better to use for an address allowlist: a mapping or an array? Why?
mapping: save gas
11. Why shouldn’t tx.origin be used for authentication? man in the middle attack
12. What hash function does Ethereum primarily use? keccak256
15. What is the difference between assert and require?
- assert: return the first four bytes of keccak256("Panic(uint256)") and error code, test internal error, invariants, 
  consume all gas
- require: return the abi encoding of the error fn Error(string), used for validating inputs, return values
  return only unused gas, so use it as early as possible
18. What is the minimum amount of Ether required to run a solo staking node? 32
19. What is the difference between fallback and receive?
    fallback: for all other txs or eth transfers when receive() isn't available: calldata might not empty
    receive: exclusively for receiving plain eth: executed on a call to the contract with empty calldata, must declared as payable
26. How can an ERC1155 token be made into a non-fungible token? set max supply to 1

# Medium
1. What is the difference between transfer and send? Why should they not be used? 
- send: cost 2300 gas, return bool
- transfer: cost 2300 gas, revert when fail
- They shoud not be used becase they imply a fixed gas cost, if you use those gas to do any operation and they success
but in the future the gas cost for those operations might increase -> fail
2. What is a storage collision in a proxy contract? storage variables in future versions might conflict with those in the older version
3. What is the difference between abi.encode and abi.encodePacked?
- abi.encode: pad data to 32 bytes, remove ambiguity
- abi.encodePacked: encode without padding -> result is smaller but more ambiguity
4. uint8, uint32, uint64, uint128, uint256 are all valid uint sizes. Are there others? What changed with block.timestamp before and after proof of stake?
- yes: uint24, uint48...
- before pos: blocktimes comme in approximately 13 seconds (with some small variance)
- after pos: blocktimes comme in exactly 12 sec
5. What is a commit-reveal scheme and when would you use it?
- commit phase: user commit the hash of their answer + random seed, seed is to ensure the opponent can't guess the answer if the answer pool is limited
- reveal phase: user reveal the answer + random seed
- use cases: ensure user can't change their answer once they've submitted it
6. Under what circumstances could abi.encodePacked create a vulnerability?
- input contains adjacent dynamic types (strings or bytes), abi.encodePacked("a", "bc") = abi.encodePacked("ab", "c")
7. How does Ethereum determine the BASEFEE in EIP-1559? based on network demand (how many percent a block was filled)
8. Cold read and warm read: whether the storage slot that’s being read was previously accessed during the transaction or not. 
The first read of a storage slot during a transaction is considered is a cold read and costs 2100 gas. 
Subsequent reads to the same storage slot are considered warm reads and cost 100 gas each.
9. Describe the three types of storage gas costs for writes
- Zero to non-zero: 20000 gas + 2100 if the slot is cold
- Non-zero to non-zero/zero: 5000 gas
10. What is the difference between UUPS and the Transparent Upgradeable Proxy pattern?
- TUP: use an additional ProxyAdmin contract
- UUPS: store upgrade logic directly in implementation contract
11. If a contract delegatecalls an empty address or an implementation that was previously self-destructed, what happens? 
What if it is a low-level call instead of a delegatecall?
- Both will return success, no revert
12. What is a bonding curve: a mathematical function that connect the supply of a digital asset with it's value
## Hard
1. How does fixed point arithmetic represent numbers?
- Two parts: integer part and fraction part: k bit integer number -> p for integer part and q for fraction part
- p + a = k, a k-bit integer n would represent n/2**q, n = 37, q=4 -> actual n = 37/16 = 2.3125
2. What is an ERC20 approval frontrunning attack?
- Spend token before the new approval
- Fix: call decreaseAllowance or add current allowance/balance in the approve function
3. How many arguments can a solidity event have?
- 3 indexed toppics
- max 16 arguments
