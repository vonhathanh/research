## Account abstraction:
- allow users to use smart contract wallets instead of EOAs
- users don't need EOAs any more
- no Ethereum consensus changes

## Specs
- UserOperation: a structure that describe a transaction to be sent of behalf of a user
    - Similar to transaction with have several other fields
    - “signature” field usage is not defined by the protocol, but by each account implementation
- Sender: account contract sending a user operation
- EntryPoint: a singleton contract to execute bundles of UserOperations. Bundlers/Clients whitelist the supported entrypoint
- Bundler: a node that can handle UserOperations
- Paymaster: a contract agrees to pay for the tx, instead of sender

Bundler send PackedUserOperation to EntryPoint contract, EP contract calls AccountCount.validateUserOp()