pragma solidity ^0.8.13;

contract Pairing {
    function run(uint256[12] memory input) public view returns (bool) {
        assembly {
            let success := staticcall(gas(), 0x08, input, 0x0180, input, 0x20)
             if success {
                return (input, 0x20)
             }
        }
        revert("wrong pairing");
    }
}