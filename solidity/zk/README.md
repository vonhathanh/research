## Notes
- calldata indicates data is stored in memory (heap) not stack because array data can be infitely large. Call data is usally transaction's data
- String concatenation wasn't supported until sol 0.8.12
- String can't be indexed and .length like array
- View is different with Pure, view -> read only, read the contract's state, pure -> no need to read anything from the contract
- Array: pop() doesnt return the removed item
- delete array[i] can't delete array element (can set it to 0, array's length is the same)
- We must use pop() swap in order to remove an element
- Private func and variables can't be seen in child contract while intenal fn can
- Internal functions do not have a function selector
- function selector make transaction smaller instead of using full func name
- fallback fn doesn't have fn selector

## Checklist
- Division before multiplication (don't)
- Not following check-effects-iteration: call another contract or sending ETH should be the last operation in a fn
- Should not use transfer() or send(): they introduce fixed gas cost, which can change if new EIPs are approved
- Don't use tx.origin unless you have to: if user is tricked into calling a malicious contract and we use tx.origin -> we thought that call was from the user
- Not determine input range for public functions (by require())
- Missing logs or incorrectly indexed logs
- Rounding in the wrong direction when division: Always round so the user loses or the protocol gains.
- Using _msgSender() in contracts that do not support metatransactions (don't)
- Whenever a user has tokens being transferred from them, the user should always be required to pass data that specifies the maximum amount they are willing to send