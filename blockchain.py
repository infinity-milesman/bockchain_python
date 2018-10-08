blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_transaction_value():
    """ Returns  the user input  as float """
    return float(input("Your transaction amount please:"))


def get_user_choice():
    """"""
    user_input = input("Your choice:")
    return user_input


def add_value(transaction_amount, last_transaction = [1]):
    """ Add the last value and current value to the blockchain """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


# txn_value = get_user_input()
#
# add_value(txn_value)
#
# txn_value = get_user_input()
# add_value(txn_value, get_last_blockchain_value())
#
# txn_value = get_user_input()
# add_value(txn_value, get_last_blockchain_value())
# print(blockchain)


def print_blockchain_elements():
    """Output the blockchain elements to the console."""
    for block in blockchain:
        print("Outputing block:")
        print(block)


while True:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Output th blockchain blocks")
    print("q: Qui t")
    user_choice = get_user_choice()
    if user_choice == '1':
        txn_value = get_transaction_value()
        add_value(txn_value, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice in ('q','Q'):
        break
    else:
        print("Input was invalid, please pick a value from the list")





print("Done")
