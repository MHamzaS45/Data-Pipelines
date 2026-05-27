from crypto_wallet import CryptoWallet

from crypto_wallet import CryptoWallet


wallet = CryptoWallet("Bruhful")

# call ze methods
wallet.deposit(13)
wallet.withdraw(11)
wallet.deposit(14)


wallet.check_balance()
wallet.transaction_history()
wallet.check_balance()
wallet.transaction_history()  
wallet.withdraw(20)  # should show insufficient balance
# brokeness calculator

if wallet.check_balance() == 0:
    print("Ya Broke.")
print("Wallet Owner:", wallet.owner)