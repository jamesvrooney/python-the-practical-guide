blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


add_value(7.6)
add_value(4.5, get_last_blockchain_value())
add_value(6.1, get_last_blockchain_value())
