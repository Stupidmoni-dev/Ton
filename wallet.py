import os
from tonapi import Tonapi  # Replacing TonapiClient
from tonsdk.wallet import WalletV4R2  # Replacing WalletV4R2 from tonutils
from tonsdk.utils import to_nano  # Utility for handling TON values
import asyncio

def create_new_wallet():
    API_KEY = os.getenv('API_KEY')
    IS_TESTNET = os.getenv('IS_TESTNET') == 'True'
    
    client = Tonapi(API_KEY)  # Using Tonapi instead of TonapiClient
    wallet = WalletV4R2()
    
    # Generate a new wallet with a mnemonic
    mnemonic = wallet.mnemonic
    return wallet, mnemonic

async def deploy_wallet(mnemonic):
    API_KEY = os.getenv('API_KEY')
    IS_TESTNET = os.getenv('IS_TESTNET') == 'True'

    client = Tonapi(API_KEY)
    
    # Recover wallet from mnemonic
    wallet = WalletV4R2(mnemonic=mnemonic)
    
    # Deploy the wallet (replace `deploy` with the actual method from tonsdk)
    tx_hash = await wallet.deploy(client)  # Assuming `deploy` is async and requires a client

    return tx_hash, wallet.address.to_string()  # Use `to_string()` instead of `to_str()`
