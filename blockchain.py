# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    # Returning the last value of the current blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

#This function accepts the arguments
#One required one (transaction_amount) and one optional one (last_transaction)
#The optional one is optional becasue the default value => [1]


def add_transaction(transaction_amount,last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :transaction_amout: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]
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
add_transaction(tx_amount)

# Get the second & third transaction input and add the value to the blockchain
while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the block chain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    print('Choice registered!')

print('Done!')
