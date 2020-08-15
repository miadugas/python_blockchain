# Initializing our (empty) blockchain list
genesis_block = {
        'previous_hash':'', 
        'index': 0, 
        'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Mia'


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    # Returning the last value of the current blockchain
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts the arguments
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional becasue the default value => [1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of the coins sent with the transaction (default 1.0)
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
        }
    open_transactions.append(transaction)
    

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash':hashed_block, 
        'index': len(blockchain), 
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user(a new transaction amount) as a float"""
    # Get the user input, transform it from a string to a flost and store it
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)
# Get the first transaction input and add the value to the blockchain
# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

# Loop logic to verify the chain
def verify_chain():
# Verify the current blockchain and return True if its valid and False otherwise
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True
    #block_index = 0
    # is_valid = True
    # for block_index in range(len(blockchain)):
    #     if block_index == 0:
    #         continue
    #     elif blockchain[block_index][0] == blockchain[block_index -1]:
    #         is_valid = True
    #     else:
    #         is_valid = False

    # another way to write the above
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index -1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    #return is_valid
waiting_for_input = True

# Get the second & third transaction input and add the value to the blockchain
while waiting_for_input:
    print('Please choose an option...')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # grab tuple data
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        # Make sure that no one tries to "hack" the blockchain if its empty
        if len(blockchain) >=1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Mia', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        # This will lead to the loop to exisit because its running condition
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        # Break out of the loop
        break
else:
    print('User has left!')


print('Done!')
