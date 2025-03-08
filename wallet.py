import os
from tonapi import TonAPI  # Corrected import
from tonsdk.wallet import WalletV4R2
from tonsdk.utils import to_nano
import asyncio

def create_new_wallet():
    API_KEY = os.getenv('API_KEY')
    IS_TESTNET = os.getenv('IS_TESTNET') == 'True'
    
    client = TonAPI(API_KEY)  # Using TonAPI instead of TonapiClient
    wallet = WalletV4R2()

    # Generate a new wallet with a mnemonic
    mnemonic = wallet.mnemonic
    return wallet, mnemonic

async def deploy_wallet(mnemonic):
    API_KEY = os.getenv('API_KEY')
    IS_TESTNET = os.getenv('IS_TESTNET') == 'True'

    client = TonAPI(API_KEY)
    
    # Recover wallet from mnemonic
    wallet = WalletV4R2(mnemonic=mnemonic)
    
    # Check if `deploy` requires additional parameters
    try:
        tx_hash = await wallet.deploy(client)  # Assuming `deploy` is async
    except AttributeError:
        print("Error: `deploy` method might not exist. Check tonsdk documentation.")
        return None, None

    return tx_hash, wallet.address.to_string()
