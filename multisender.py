import random
import time

from solana.rpc.api import Client
from solana.transaction import Transaction

from solders.pubkey import Pubkey
from solders.keypair import Keypair

from solders.system_program import TransferParams, transfer


def send_tx(address_to: str):

    address_to = Pubkey.from_string(f'{address_to}')
    address_with_balance = Pubkey.from_string('Cюда аддресс кошелька с которого раскид')
    private_key_balance = Keypair.from_base58_string('Сюда приватник кошелька с котороо раскид')

    amount_in_sol = random.uniform(0.005, 0.009)

    amount_lamports = int(amount_in_sol * 10**9)

    transfer_tx = Transaction().add(transfer(TransferParams(from_pubkey=address_with_balance,
                                                            to_pubkey=address_to,
                                                            lamports=amount_lamports)))
    client = Client('https://api.mainnet-beta.solana.com')

    receipt = client.send_transaction(transfer_tx, private_key_balance).value
    if receipt:
        return f'Success send SOL {amount_in_sol} to {address_to}| Tx: https://solscan.io/tx/{receipt}'
    else:
        return f'Not get receipt, no transaction for {address_to}'


if __name__ == '__main__':
    with open('address_sol_multisend.txt', 'r') as file:
        success_send = 0
        fail_send = 0

        for address in file:
            res = send_tx(address.rstrip())
            print(res)
            if 'Success' in res:
                success_send += 1
            else:
                fail_send += 1

            print(f'Sleep 8 - 15 seconds')
            time.sleep(random.randint(8, 15))

        print(f'Успешное кол-во кошельков: {success_send} | Не успешное: {fail_send}')
        print(f'Multisend завершен | This shit make Toby for 0xLeo')








