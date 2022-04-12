from brownie import accounts, config, network , MockV3Aggregator , Contract

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
        contract = contract_type[-1]
        # MockV3Aggregator[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        # address
        # abi
        contract = Contract.from_abi(contract_type.name,contract_address,contract_type.abi)
        # MockV3Aggregator.abi
    return contract


DECIMALS = 8
INITIAL_VALUE = 200000000000
#10**8

def deploy_mocks(decinals = DECIMALS,initial_value = INITIAL_VALUE):
    account = get_account()
    mock_price_feed = MockV3Aggregator.deploy(decinals,initial_value,{"from": account})
    print ("Deployed!")