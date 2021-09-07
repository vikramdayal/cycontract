'''Contracts Package
Support for maintaining contracts. All of the features can be invoked from the cycontracts notebook.
'''

import getpass
_contracts = []


def list_contracts():
    print("name             ", "author")
    print("-----------------", "-------------------------------")
    for c in _contracts:
        print(f'{c.name:15}   {c.author:30}')


def add_contract(contract):
    _contracts.append(contract)


class Contract:
    def __init__(self, name):
        self.name = name
        self.author = getpass.getuser()
        self.serialized = None

