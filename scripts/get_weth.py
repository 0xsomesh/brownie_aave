from scripts.helpful_scripts import get_account, config, network
from brownie import interface


def main():
    get_weth()


def get_weth():
    account = get_account()
    weth = interface.IWeth(
        config['networks'][network.show_active()]['weth_token'])
    tx = weth.deposit({'from': account, 'value': 0.1 * 10 ** 18})
    print('received 0.1 weth')
    tx.wait(1)
