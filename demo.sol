// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Импортируем стандарт для ERC20 токена
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenTransfer {
    // Адрес ERC20 токена
    address public tokenAddress;

    // Конструктор, принимающий адрес ERC20 токена
    constructor(address _tokenAddress) {
        tokenAddress = _tokenAddress;
    }

    // Функция для отправки токенов на другой счет
    function transferTokens(address to, uint256 amount) external {
        // Создаем экземпляр ERC20 токена
        IERC20 token = IERC20(tokenAddress);

        // Передаем токены с текущего счета на указанный счет
        require(token.transfer(to, amount), "Transfer failed");
    }
}

// contract UserBalanceChecker {
//     // Функция для получения баланса пользователя
//     function getUserBalance(address user) public view returns (uint256) {
//         return user.balance;
//     }
// }