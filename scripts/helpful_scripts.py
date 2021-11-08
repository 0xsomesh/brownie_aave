from brownie import network, accounts, config

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork-dev']
LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development", 'mainnet-fork', "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active(
    ) in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active(
    ) in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]

    return accounts.add(config['wallets']['from_key'])
