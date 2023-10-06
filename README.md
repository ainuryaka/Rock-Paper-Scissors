# Rock-Paper-Scissors

This Ethereum smart contract implements a secure Rock-Paper-Scissors game that's ready for deployment on the blockchain. Here's how the game works:

- Two players can register and place bets.
- Each player selects a move and a password, sending the hash of the combined string to the contract.
- When both players make their moves, they reveal what they've played by sending their move and password in clear text.
- The contract verifies that the hash of the received input data matches the stored one.
- Once both players reveal their moves, the contract determines the winner and distributes the total bets. In case of a draw, each player receives their bet back.

Key Features:
- Player registration with MetaMask.
- Secure hashing of moves and passwords.
- Fair resolution of the game.
- Public state variables and auxiliary functions for game information.

## Functions Available

- `register()`: Register players in MetaMask.
- `play(bytes32 encrMove)`: Submit moves (hashed) with a bet.
- `reveal(string memory clearMove)`: Reveal your move after playing.
- `getOutcome()`: Get the game result and rewards.
- `getContractBalance()`: Check the current betting pool.
- `whoAmI()`: Find your player's ID (1 or 2 if registered, 0 if not).
- `bothPlayed()`: Check if both players have played.
- `bothRevealed()`: Check if both players have revealed their moves.
- `revealTimeLeft()`: Get the remaining time for the reveal phase.

Feel free to explore the code and try out the game on the Ethereum blockchain.

## Usage

1. Register as Player 1 or Player 2 using MetaMask.
2. Send a bet (0.0001 tBNB or more) to the contract.
3. Submit your move using `play(bytes32 encrMove)` with your move hashed.
4. After both players have played, reveal your move with `reveal(string memory clearMove)`.
5. Determine the outcome and collect your rewards with `getOutcome()`.

## Contributors

- [Kurmanbay Abylkair, Orynbekova Ainura, Kassymkhanov Nursultan]

