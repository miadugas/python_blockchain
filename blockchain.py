# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returning the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount,last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :transaction_amout: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction,transaction_amount])

def get_user_input():
    """ Returns the input of the user(a new transaction amount) as a float"""
    user_input = float(input('Your transaction amount please: '))
    return user_input

# Get the first transaction input and add the value to the blockchain
tx_amount=get_user_input()
add_value(tx_amount)

# Get the second & third transaction input and add the value to the blockchain
while True:
    tx_amount=get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

print('Done!')
