import contracts


def run_test():
    c1 = contracts.Contract("test1")
    contracts.add_contract(c1)
    c2 = contracts.Contract("test2")
    contracts.add_contract(c2)
    contracts.list_contracts()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
