brownie init 
Lottary.sol in contract
test_lottery.py to test

delete mainnet-fork from brownie builtin 
    brownie networks delete mainnet-fork

add our own coustom mainnet-fork using alchemy
    brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/<key> accounts=10 mnemonic=brownie port=8545

import openzepplin for onlyowner modifier