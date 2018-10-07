blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of current blockchain """
    return blockchain[-1]


def get_user_input():
    """ Returns  the user input  as float """
    return float(input("Your transaction amount please:"))


def add_value(transaction_amount, last_transaction = [1]):
    """ Add the last value and current value to the blockchain """
    blockchain.append([last_transaction, transaction_amount])


txn_value = get_user_input()

add_value(txn_value)

txn_value = get_user_input()
add_value(txn_value, get_last_blockchain_value())

txn_value = get_user_input()
add_value(txn_value, get_last_blockchain_value())
print(blockchain)