from brownie import SimpleStorage,accounts,config

def read_contract():
   xcontact=  SimpleStorage[-1]
   print(xcontact.retrieve())

def main():
    read_contract()