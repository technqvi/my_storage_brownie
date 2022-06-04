from brownie import accounts,config,SimpleStorage,network
#import os
def deploy_simple_storage():
  account=get_account()
  # account=accounts.add(os.getenv("PRIVATE_KEY"))     OR  account=accounts.add(config["wallets"]["from_key"])
  x_contract=SimpleStorage.deploy({"from":account})
  stored_value=x_contract.retrieve()
  print(f'Current :{stored_value}')

  transaction=x_contract.store(9999,{"from":account})
  transaction.wait(1)
  updated_stored_value=x_contract.retrieve() 
  print(f'Update :{updated_stored_value}')
  
def get_account():
  if network.show_active== "development":
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])


def main():
    print("Hello, Implement ETH using Bronwie-Python Framework")
    deploy_simple_storage()