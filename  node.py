class Node:
    def __init__(self):
        self.blockchain =[]

    def get_transaction_value(self):
#Returns the input of the user(a new transaction amount) as a float
    # Get the user input, transform it from a string to a flost and store it
        tx_recipient = input('Enter the recipient of the transaction:')
        tx_amount = float(input('Your transaction amount please: '))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        """Prompts the user for a choice and return it."""
        user_input = input('Your choice: ')
        return user_input


    def print_blockchain_elements(self):
    # Output the blockchain list to the console
        for block in self.blockchain:
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)
# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

    def listen_for_input(self):
        # Loop logic to verify the chain
        waiting_for_input = True

        # A while loop for the user input interface
# It's a loop that exits once waiting_for_input becomes False or when break is called
        while waiting_for_input:
            print('Please choose an option...')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
    # print('h: Manipulate the chain')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
        # grab tuple data
                recipient, amount = tx_data
        # Add the transaction amount to the blockchain
                if add_transaction(recipient, amount=amount):
                    print('Added Transaction!')
                else:
                    print('Transaction Failed! Please verify your balance before resending')
                    print(open_transactions)
                elif user_choice == '2':
                    if mine_block():
                        open_transactions = []
                        save_data()
                elif user_choice == '3':
                        self.print_blockchain_elements()
                elif user_choice == '4':
                    verifier = Verification()
                    if verifier.verify_transactions(open_transactions, get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
    # elif user_choice == 'h':
    #     # Make sure that no one tries to "hack" the blockchain if its empty
    #     if len(blockchain) >= 1:
    #         blockchain[1] = {
    #             'previous_hash': '',
    #             'index': 0,
    #             'transactions': [{'sender': 'Chris', 'recipient': 'Mia', 'amount': 100.0}]
    #         }
                    elif user_choice == 'q':
        # This will lead to the loop to exisit because its running condition
                        waiting_for_input = False
                        else:
                        print('Input was invalid, please pick a value from the list!')
                        verifier = Verification()
                    if not verifier.verify_chain(blockchain):
                    self.print_blockchain_elements()
                    print('Invalid blockchain!')
        # Break out of the loop
                    break
                    print('Balance of {}: {:6.2f}'.format('Mia', get_balance('Mia')))
                else:
                    print('User left!')


                    print('Done!')
