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


def get_transaction_value():
    """ Returns the input of the user(a new transaction amount) as a float"""
    # Get the user input, transform it from a string to a flost and store it
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():        
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

# Get the first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

# Get the second & third transaction input and add the value to the blockchain
while True:
    print('Please choose an option')
    print('1: Add a new transaction value')
    print('2: Output the block chain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()


print('Done!')
