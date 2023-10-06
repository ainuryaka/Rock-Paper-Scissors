from flask import Flask, render_template, request, redirect
import random
from web3 import Web3

app = Flask(__name__)
bsc_rpc_url = "https://data-seed-prebsc-1-s1.binance.org:8545"

w3 = Web3(Web3.HTTPProvider(bsc_rpc_url))

class Client:
    def __init__(self, address, countWins=0, winning_price=0):
        self.address = address
        self.countWins = countWins
        self.winning_price = winning_price

    def increase_wins(self):
        self.countWins += 1

    def add_winning_price(self, amount):
        self.winning_price += amount

    def __str__(self):
        return f"Client address: {self.address}, Wins: {self.countWins}, Winning Price: {self.winning_price}"

client = Client(address="")

def get_computer_move():
    options = ["rock", "paper", "scissors"]
    return options[random.randint(0,2)]

def get_winner(player_choice, computer_choice):
    winner = "computer"

    if player_choice == computer_choice:
        winner = "tie"
    if player_choice == "rock" and computer_choice == "scissors":
        winner = "player"
        client.increase_wins()
        client.add_winning_price(0.002)
    if player_choice == "scissors" and computer_choice == "paper":
        winner = "player"
        client.increase_wins()
        client.add_winning_price(0.002)
    if player_choice == "paper" and computer_choice == "rock":
        winner = "player"
        client.increase_wins()
        client.add_winning_price(0.002)

    if winner == 'computer':
        client.countWins -= 1
        client.winning_price -= 0.001

    return winner

@app.route('/')
def authorization():
    return render_template('login.html')

@app.route('/startGame', methods=['GET', 'POST'])
def index():
    if client.address == "":
        address = request.form['address']
        client.address = address

    print(client)
    return render_template("index.html", winning = client.winning_price, countWin = client.countWins)

@app.route('/rps/<choice>')
def rps(choice):
    player_choice = choice.lower()
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)
    return render_template("rps.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    client.address = ""
    client.countWins = 0
    client.winning_price = 0
    return redirect('/')

@app.route('/transfer', methods=['POST'])
def transaction():
    if client.countWins > 0:
        # Private key of the sender (for signing the transaction)
        private_key = "93d1f27d42e82cf6eca33e116f5651751416f98311d13a99ec8d5fbae0396bbb"

        # Amount to send (in wei)
        amount_wei = w3.to_wei(client.winning_price, 'ether')  # For example, sending 1 BNB

        # Get the current nonce of the sender (number of transactions from this address)
        sender_address = "0x316808C61411C24c1578E51F356fdC8ebD123649"
        nonce = w3.eth.get_transaction_count(sender_address)

        # Create a transaction
        transaction = {
            'to': client.address,
            'value': amount_wei,
            'gas': 21000,  # Gas limit for a basic transaction
            'gasPrice': w3.to_wei('10', 'gwei'),  # Gas price in Gwei
            'nonce': nonce,
        }

        # Sign the transaction using the sender's private key

        signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

        # Send the transaction to the network
        tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        print(f"Transaction sent. Transaction hash: {tx_hash.hex()}")
    else:
        private_key = request.form['private_key']
        print(private_key)
        amount_wei = w3.to_wei(abs(client.winning_price), 'ether')
        sender_address = client.address
        nonce = w3.eth.get_transaction_count(sender_address)
        transaction = {
            'to': "0x316808C61411C24c1578E51F356fdC8ebD123649",
            'value': amount_wei,
            'gas': 21000,  # Gas limit for a basic transaction
            'gasPrice': w3.to_wei('10', 'gwei'),  # Gas price in Gwei
            'nonce': nonce,
        }

        signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

        # Send the transaction to the network
        tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        print(f"Transaction sent. Transaction hash: {tx_hash.hex()}")
    return redirect("/startGame")


if __name__ == "__main__":
    app.run()
