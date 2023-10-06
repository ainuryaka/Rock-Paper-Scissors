// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenTransfer {
    // Address of the ERC20 token
    address public tokenAddress;

    //Constructor that accepts the ERC20 token address
    constructor(address _tokenAddress) {
        tokenAddress = _tokenAddress;
    }

    // Function to send tokens to another account
    function transferTokens(address to, uint256 amount) external {
        // Create an instance of the ERC20 token
        IERC20 token = IERC20(tokenAddress);

        // Transfer tokens from the current account to the specified account
        require(token.transfer(to, amount), "Transfer failed");
    }
}

// contract UserBalanceChecker {
//     // Function to get user balance
//     function getUserBalance(address user) public view returns (uint256) {
//         return user.balance;
//     }
// }
