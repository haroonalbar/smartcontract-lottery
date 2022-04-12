from brownie import accounts, config, network , MockV3Aggregator

FORKED_LOCAL_ENVITONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCAHIN_ENVIRONMENT = ["development", "dog"]


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCAHIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVITONMENTS
    ):
         return accounts[0]
    # default
    return accounts.add(config["wallets"]["from_key"])

contract_to_mock = contract_to_mock{
    "eth_usd_price_feed": MockV3Aggregator
}

def get_contract(contract_name):
    """This function will grab the contract addresses from the brownie config
    if defined, otherwise, it will deploy a mock version of that contract, and
    return that mock contract.
        Args:
            contract_name (string)
        Returns:
            brownie.network.contract.ProjectContract: The most recently deployed
            version of this contract.
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCAHIN_ENVIRONMENT:
        if len(contract_type) <= 0:
            #MockV3Aggregator.length
            deploy_mocks()