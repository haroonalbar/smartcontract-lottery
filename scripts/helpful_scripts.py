from brownie import accounts, config, network

FORKED_LOCAL_ENVITONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCAHIN_ENVIRONMENT = ["development", "dog"]


def get_account():
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if (
        network.show_active() in LOCAL_BLOCKCAHIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVITONMENTS
    ):
        return accounts[0]
    # default
    return accounts.add(config["wallets"]["from_key"])
