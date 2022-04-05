# 0.019 aprox eth equal to 50 usd
from brownie import Lottery, accounts, network, config
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    # assert lottery.getEntranceFee() > Web3.toWei(0.013, "ether")
    # assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")
